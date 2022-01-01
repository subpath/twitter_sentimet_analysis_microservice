import logging
import uuid

from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=False,
    pool_size=20,
    max_overflow=100,
    pool_recycle=3600,
)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()


class Twiiter_sentiment(Base):
    __tablename__ = "twitter_sentiment_data"

    id = Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    search_query = Column(String)
    twitter_id = Column(String)
    tweet_original = Column(String)
    tweet_translated = Column(String)
    lang = Column(String)
    created_at = Column(DateTime, nullable=False)
    geo = Column(String)
    reply_count = Column(Integer)
    retweet_count = Column(Integer)
    likes_count = Column(Integer)

    user_id = Column(String)
    user_name = Column(String)
    user_location = Column(String)
    user_description = Column(String)
    user_verified = Column(Boolean)
    user_followers_count = Column(Integer)
    user_friends_count = Column(Integer)

    polarity = Column(Float)
    subjectivity = Column(Float)

    def __init__(
        self,
        search_query,
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
    ):
        self.search_query = search_query
        self.twitter_id = twitter_id
        self.tweet_original = tweet_original
        self.tweet_translated = tweet_translated
        self.lang = lang
        self.created_at = created_at
        self.geo = geo
        self.reply_count = reply_count
        self.retweet_count = retweet_count
        self.likes_count = likes_count

        self.user_id = user_id
        self.user_name = user_name
        self.user_location = user_location
        self.user_description = user_description
        self.user_verified = user_verified
        self.user_followers_count = user_followers_count
        self.user_friends_count = user_friends_count

        self.polarity = polarity
        self.subjectivity = subjectivity


def save_sentiment(
    search_query,
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
):
    try:
        sentiment = Twiiter_sentiment(
            search_query,
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

        Session.add(sentiment)
        Session.commit()
        return True
    except Exception as e:
        Session.rollback()
        logging.error(e)
        return False
