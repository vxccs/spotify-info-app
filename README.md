# Spotify Info App

#### [▶️ Live demo](https://spotify-info-app.herokuapp.com/)

This project is a web app that makes use of Spotify's Web API to present information about any track or album. This includes various audio features for a single track, like **Danceability**, **Energy**, **Popularity**, **Tempo**, **Instrumentalness**, and **Speechiness**, among others. Simply pasting a link will fetch the required information from Spotify and display it for the user.

The app was created with Flask, Python, HTML and CSS, and a little JavaScript.

# How it works

A user can paste a link for a Spotify album or track, the app will then parse that link to confirm it's a valid link, and get the item's ID to make a request to the API for the information required, sending the data to the pages which will then render the content.

If an album, the page will present links to every song in its tracklist. Each track presents a collection of various audio features that describe the song. If anything goes wrong in the process, the app will generate custom error pages.

Each individual page is created with HTML, using Jinja syntax for templating and handling of the variable data. As well as CSS for the visual aspect, inspired by Spotify's own design language.

Due to Spotify's API limitations, each access token is only valid for an hour, this is why the app makes usage of APScheduler to generate a new valid token every hour, keeping the app functional. Also defined in a helpers Python file, fhe app has various custom functions, including a URL parser that utilizes Regex patterns, as well as other functions used as Jinja filters, mainly for string and number formatting.

# Possible improvements

- Search function in addition to pasting links
- Display artist data
- Display playlist data
