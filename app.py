import requests
from flask import Flask, redirect, render_template, request, url_for
from helpers import *
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os

# configure application
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# create custom filters
app.jinja_env.filters["sectomins"] = sectomins
app.jinja_env.filters["sectomins_format"] = sectomins_format
app.jinja_env.filters["date_format"] = date_format
app.jinja_env.filters["mode_format"] = mode_format
app.jinja_env.filters["decimals_format"] = decimals_format
app.jinja_env.filters["key_format"] = key_format

# format html jinja blocks
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks  = True

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = ""

def token():

    # POST
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    global ACCESS_TOKEN
    ACCESS_TOKEN = auth_response_data['access_token']

token()
scheduler = BackgroundScheduler()
scheduler.add_job(token, 'interval', seconds=3590)
scheduler.start()

# index page
@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        
        URL = parse_url(request.form.get("item-id"))

        if not URL:
            # create a 404 page
            return redirect("/")
        
        if URL["type"] in ["album", "single", "compilation"]:
            return redirect(url_for("album", file_id=URL["id"]))
        elif URL["type"] == "track":
            return redirect(url_for("track", file_id=URL["id"]))
        else:
            # create a 404 page
            return redirect("/")
    
    else:
        return render_template("index.html")


# album page
@app.route("/album/<file_id>")
def album(file_id):

    response = requests.get(
        f"https://api.spotify.com/v1/albums/{file_id}",
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
            }
        )
    response_data = response.json()

    return render_template("album.html", data=response_data)


# track page
@app.route("/track/<file_id>")
def track(file_id):

    track = requests.get(
        f"https://api.spotify.com/v1/tracks/{file_id}",
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
            }
        )
    track_data = track.json()

    features = requests.get(
        f"https://api.spotify.com/v1/audio-features?ids={file_id}",
        headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}"
            }
        )
    features_data = features.json()

    return render_template("track.html", track=track_data, features=features_data["audio_features"][0])


# audio features page
@app.route("/about")
def about():
    return render_template("about.html")

# redirect if no id
@app.route("/album/")
@app.route("/track/")
def default():
    return redirect("/")


# error handling 

@app.errorhandler(400)
def bad_request(e):
    return render_template('error.html', error="Bad request!", message="You've sent a bad request."), 400


@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', error="Forbidden!", message="You do not have access to this page."), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error="Page not found!", message="What you were looking for is just not there."), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error="Something went wrong!", message="Oops... the server is having some issues, sorry!"), 500


@app.errorhandler(503)
def internal_server_error(e):
    return render_template('error.html', error="Something went wrong!", message="Oops... we seem to have made a mistake, sorry!"), 503


@app.errorhandler(Exception)
def handle_exception(e):
   return render_template('error.html', error="Something went wrong!", message="Oops... we seem to have made a mistake, sorry about that!")

atexit.register(scheduler.shutdown)