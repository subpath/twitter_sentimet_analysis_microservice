# Microservice for Twitter Real time data collection and sentiment analysis

#### Stack: TwitterAPI + Flask + Nameko + Postgresql + Textblob

## What it does:
 1. It receives POST request with instruction of which twitter it needs to collect
 2. Then it opens socket connection with Twitter API and starts to receive real time twitter data
 3. Each tweet assigned with it sentiment score with help of TextBlob
 4. All data then goes to PostgreSQL database

## Main features:
 * Because it uses [Nameko]('https://github.com/nameko/nameko') and [RabbitMQ]('https://www.rabbitmq.com')
 you can asynchronously run many different tasks and collect different topics.
 * Because it based on [Flask]('http://flask.pocoo.org') you can easily connect this with other services that will communicate with this service by POST requests
 * For each tweet service assign sentiment score using [TextBlob]('https://textblob.readthedocs.io/en/dev/') and store
 it to the [PostgreSQL]('https://www.postgresql.org') so latter you can perform analysis on that.
 * It scalable and expandable - you can easily add other sentiment analysis tools or create visualization or
 web interface because it based on Flask

#### Example of POST request json

```json
{
"duration": 60,
"query": ["Bitcoin", "BTC", "Cryptocurrency", "Crypto"],
"translate": false
}

```
where duration is how many minutes you what collect streaming twitter data,
query is list of search queries that Twitter API will use to send you relevant tweets,
translate is boolean in case False will collect only english tweets,
otherwise service will try machine translation from TextBlob


## Instalation:
1. Clone or download this repository:
`git clone`
2. Create virtual environment and install dependencies:

```
cd twitter_sentiment_analysis_microservice

virtualenv env --python python3

source env/bin/activate

pip install -r requirements.txt
```

3. Setup PostgreSQL:

 [Please find instruction here](https://gist.github.com/subpath/21d51f985cb079252544b880caf2adfa)

4. Get your Twitter credentials

 [You can get your Twitter credentials here](https://apps.twitter.com)

5. Install RabbitMQ:

instruction for mac: https://www.rabbitmq.com/install-homebrew.html

6. Run RabbitMQ: `sudo rabbitmq-server`

7. Run Nameko: `nameko run service --config ./config.yaml`

8. Run Flask (in a different terminal): `python app.py`

##### Whoa! It's finally running!

Now it ready to receive requests:

By default you can send POST requests to `127.0.0.1:5000/collect`
