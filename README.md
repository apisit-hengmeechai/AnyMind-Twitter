# AnyMind-Twitter
AnyMind project examination

Install
-----------
create virtual environment:

    $ virtualenv -p python3 env

activate virtual environment:

    $ source env/bin/activate

install requirement libs using pip:

    $ pip install -r requirement.txt
----
Configuration
-----------
please change application configuration in settings.py:

    PORT= 8888 # Server PORT
    CONSUMER_API_KEY= 'TWITTER CONSUMER KEY' #TWITTER CONSUMER KEY
    CONSUMER_API_SECRET_KEY= 'TWITTER CONSUMER SECRET' #TWITTER CONSUMER SECRET
    AUTH_URL= 'https://api.twitter.com/oauth2/token' #TWITTER OAUTH2.0 URL
    SEARCH_URL= 'https://api.twitter.com/1.1/search/tweets.json' #TWITTER SEARCH URL
    USER_TIMELINE_URL= 'https://api.twitter.com/1.1/statuses/user_timeline.json' #TWITTER USER TIMELINE URL
----
Running
-----------
    $ python app.py
----
Get User timeline
-----------
* **URL:**

URL

    /users/{twitter_username}
URL (example)

    /users/{twitter_username}?limit=40


* **Method:**

  `GET`

* **Params**

| Attribute       | Type    | Required | Description                  |
|:----------------|:--------|:---------|:-----------------------------|
| `limit`         | integer |   no     | limit response default is 30 |

* **Example Response:**
```json
[
  {
    "contributors": null,
    "coordinates": null,
    "created_at": "Tue Oct 29 19:39:40 +0000 2019",
    "entities": {
      "hashtags": [],
      "symbols": [],
      "urls": [],
      "user_mentions": [
        {
          "id": 2244994945,
          "id_str": "2244994945",
          "indices": [
            3,
            14
          ],
          "name": "Twitter Dev",
          "screen_name": "TwitterDev"
        }
      ]
    },
    "favorite_count": 0,
    "favorited": false,
    "geo": null,
    "id": 1189265562821640193,
    "id_str": "1189265562821640193",
    "in_reply_to_screen_name": null,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    ...
  }
]
```
----
Search by hashtag
-----------
* **URL:**

URL

    /hashtags/{{hashtag}}

URL (example)

    /hashtags/{{hashtag}}?limit=40


* **Method:**

  `GET`

* **Params**

| Attribute       | Type    | Required | Description                  |
|:----------------|:--------|:---------|:-----------------------------|
| `limit`         | integer |   no     | limit response default is 30 |

* **Example Response:**
```json
{
  "search_metadata": {
    "completed_in": 0.049,
    "count": 20,
    "max_id": 1204391777924304898,
    "max_id_str": "1204391777924304898",
    "next_results": "?max_id=1204390872592404479&q=%23python&count=20&include_entities=1",
    "query": "%23python",
    "refresh_url": "?since_id=1204391777924304898&q=%23python&include_entities=1",
    "since_id": 0,
    "since_id_str": "0"
  },
  "statuses": [
    {
      "contributors": null,
      "coordinates": null,
      "created_at": "Tue Dec 10 13:25:51 +0000 2019",
      "entities": {
        "hashtags": [
          {
            "indices": [
              118,
              125
            ],
            "text": "Python"
          }
        ],
        "symbols": [],
        ...
      }
    }
  ]
}
```
----