# Spotify Info App (CS50 Final Project)

#### Video Demo:

#### [▶️ Live demo](https://spotify-info-app.herokuapp.com/)

This project is a web app that makes use of Spotify's Web API to present information about any track or album. This includes various audio features for a single track, like **Danceability**, **Energy**, **Instrumentalness**, **Popularity**, **Speechiness**, and **Tempo**, among others. Simply pasting a link will fetch the required information from Spotify and display it for the user.

The app is made with Flask, Python, HTML and CSS, and a little JavaScript.

# How it works

A user can paste a link for a Spotify album or track, the app will then parse that link with Regex patterns to validate it and get the item's ID and make a request to the API for the information required, sending the data to the pages which will render the content. If anything goes wrong in the process, the app will generate custom error pages.

Each individual page is made with HTML, using Jinja syntax for templating and handling of the variable data. As well as CSS for the visual aspect, inspired by Spotify's own design language.

Due to Spotify's API limitations, each access token is only valid for an hour, this is why the app makes usage of APScheduler to generate a new valid token every hour, keeping the app functional.

# Possible improvements

- Search function in addition to pasting links
- Display artist data
- Display playlist data
