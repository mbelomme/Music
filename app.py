from typing import Mapping
import config

from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder = "template")

@app.route('/', methods=["POST", "GET"])
def request_topsong():

    artist = request.form.get("artist")
    print(artist)

    url = "https://genius.p.rapidapi.com/search"

    querystring = {"q":artist}

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    print()
    topsong = data["response"]["hits"][0]["result"]["full_title"]
    return render_template("index.html", song = topsong)
    
if __name__ == "__main__":
    app.run(debug=True)
