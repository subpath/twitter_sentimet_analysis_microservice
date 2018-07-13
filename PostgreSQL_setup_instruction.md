# PostgreSQL setup instruction

Only for Ubuntu, because I use Ubuntu on

1. Install postgreSQL:

```
sudo apt install postgresql postgresql-contrib
```

2. Run postgreSQL:

```
sudo su - postgres

psql
```

3. Create user and database:

```
CREATE USER user_name WITH PASSWORD "pass";
ALTER USER user_name WITH SUPERUSER;
CREATE DATABASE my_db;
```

4. Create table for Twitter data:

```
CREATE TABLE twitter_sentiment_data(
    id UUID PRIMARY KEY NOT NULL,
    search_query text,
    twitter_id text,
    tweet_original text,
    tweet_translated text,
    lang text,
    created_at timestamp,
    geo text,
    reply_count integer,
    retweet_count integer,
    likes_count integer,
    user_id text,
    user_name text,
    user_location text,
    user_description text,
    user_verified boolean,
    user_followers_count integer,
    user_friends_count integer,

    polarity float,
    subjectivity float
);
```

5. If you postgreSQL is on remote server, configure as followed:
  https://blog.bigbinary.com/2016/01/23/configure-postgresql-to-allow-remote-connection.html
