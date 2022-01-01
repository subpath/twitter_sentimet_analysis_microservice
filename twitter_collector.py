import datetime
import json
import logging

from textblob import TextBlob
from tweepy.streaming import StreamListener
from unidecode import unidecode

from models.sentiment import save_sentiment


class TwitterStreamer(StreamListener):
    def __init__(self, search_query, end_time, translate):
        super(TwitterStreamer, self).__init__()
        self._end_time = end_time
        self._search_query = search_query
        self._translate = translate

    def on_data(self, data):
        """Tweet generic info."""
        try:
            data = json.loads(data)

            tweet_original = str(unidecode(data["text"]))
            lang = data["lang"]
            if self._translate:
                if lang != "en":
                    tweet_translated = str(TextBlob(tweet_original).translate(to="en"))
                else:
                    tweet_translated = str(tweet_original)
            else:
                tweet_translated = str(tweet_original)
            created_at = datetime.datetime.utcfromtimestamp(
                int(data["timestamp_ms"]) / 1000
            ).strftime("%Y-%m-%dT%H:%M:%SZ")
            twitter_id = str(data["id"])
            user = data["user"]
            geo = data["geo"]
            reply_count = data["reply_count"]
            retweet_count = data["retweet_count"]
            likes_count = data["favorite_count"]

            # User info
            user_id = str(user["id"])
            user_name = user["name"]
            user_location = user["location"]
            user_description = ["description"]
            user_verified = user["verified"]
            user_followers_count = user["followers_count"]
            user_friends_count = user["friends_count"]

            # Sentiment info
            sentiment_model = TextBlob(tweet_translated)
            polarity = sentiment_model.sentiment.polarity
            subjectivity = sentiment_model.sentiment.subjectivity

            if datetime.datetime.utcnow() > self._end_time:
                return False

            save_sentiment(
                self._search_query,
                self._end_time,
                twitter_id,
                tweet_original,
                tweet_translated,
                lang,
                created_at,
                geo,
                reply_count,
                retweet_count,
                likes_count,
                user_id,
                user_name,
                user_location,
                user_description,
                user_verified,
                user_followers_count,
                user_friends_count,
                polarity,
                subjectivity,
            )

        except KeyError as e:
            logger.error(e)

        return True

    def on_error(self, status):
        logging.error(status)
