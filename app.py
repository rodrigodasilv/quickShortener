from flask import Flask, redirect, request
from waitress import serve
import URLManager

app = Flask(__name__)


@app.route('/<shorter_code>', methods=['GET'])
def get_full_url(shorter_code):
    redirect_url = URLManager.get_url(shorter_code)
    return redirect(redirect_url)


@app.route('/', methods=['POST'])
def create_short_url():
    url = request.json['url']
    return URLManager.create_short_url(url)


serve(app, host="0.0.0.0", port=8080)
