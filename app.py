from flask import Flask, request
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {"AMQP_URI": "amqp://guest:guest@localhost"}


@app.route("/collect", methods=["POST"])
def collect():
    duration = request.json.get("duration")
    query = request.json.get("query")
    translate = request.json.get("translate")
    with ClusterRpcProxy(CONFIG) as rpc:
        rpc.collector.collect.call_async(duration, query, translate)
        return "Success"


app.run(debug=True)
