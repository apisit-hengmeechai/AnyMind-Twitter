from flask import Flask, request, Response, jsonify
from werkzeug.exceptions import abort
from settings import PORT, CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY, AUTH_URL, SEARCH_URL, USER_TIMELINE_URL
import requests, json
import urllib.parse

app = Flask(__name__)


def get_access_token():
    params = {'grant_type': 'client_credentials'}
    r = requests.post(url=AUTH_URL, params=params, auth=(
        CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY))
    access_token = r.json().get("access_token")
    if access_token != None:
        return access_token
    else:
        response = json.dumps(
            {'message': 'Can\'t get access_token please try again.'})
        abort(Response(response=response, status=500, mimetype='application/json'))


@app.route('/hashtags/<q>')
def hashtags_search(q):
    limit = request.args.get('limit', 30)
    params = {'count': limit, 'q': '#' + q}
    headers = {'Authorization': 'Bearer ' + get_access_token()}
    r = requests.get(url=SEARCH_URL, params=params, headers=headers)
    return jsonify(r.json())


@app.route('/users/<user>')
def user_timeline(user):
    limit = request.args.get('limit', 30)
    params = {'count': limit, 'screen_name': user}
    headers = {'Authorization': 'Bearer ' + get_access_token()}
    r = requests.get(url=USER_TIMELINE_URL, params=params, headers=headers)
    return jsonify(r.json())


if __name__ == '__main__':
    app.run('0.0.0.0', PORT)
