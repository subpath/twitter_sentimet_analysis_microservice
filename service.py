import datetime
import logging
from time import sleep

from nameko.rpc import rpc
from tweepy import OAuthHandler, Stream

from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from twitter_collector import TwitterStreamer


class DataCollector(object):
    name = "collector"

    @rpc
    def collect(self, duration, query, translate):
        end_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=duration)
        logger.info("end_time: {}, query: {}".format(end_time, query, translate))
        if datetime.datetime.utcnow() < end_time:
            while datetime.datetime.utcnow() < end_time:
                try:
                    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
                    twitterStream = Stream(
                        auth, TwitterStreamer(query, end_time, translate)
                    )
                    twitterStream.filter(track=query)

                except Exception as e:
                    sleep(5)
                    logging.error(e)
