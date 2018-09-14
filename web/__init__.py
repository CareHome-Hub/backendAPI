import requests
from .data.models import campaigns, touchpoints,news
import logzero
from logzero import logger

from flask import Flask, render_template, jsonify,request
logzero.logfile("./rotating-logfile.log", maxBytes=1e6, backupCount=3)
app = Flask(__name__)


@app.route("/news")
def index():
    return news.get_news_articles()

@app.route('/')
def hello_world():
    logger.info("root triggered")
    return jsonify({"status": 418, "error":"I'm a teapot"})

@app.route('/tet/v1/campaigns')
def get_campaign_listing():
    logger.info("/tet/v1/campaigns")
    search = campaigns.get_campaigns()
    logger.info("campaigns.get_campaigns()")
    if 'campaign' in request.args:
        logger.info("campaign - request.args")
        result = []
        req = request.args.get('campaign')
        for camp in search:
            if req == camp['campaign']:
                result.append(camp)
    else:
        result = search

    resp = {}
    resp["status"] = 200
    resp["result"] = result
    return jsonify(resp)


@app.route('/tet/v1/touchpoints')
def get_touchpoint_listing():
    logger.info("/tet/v1/touchpoints")
    search = touchpoints.get_touchpoints()
    if 'touchpoint' in request.args:
        logger.info("touchpoint - request.args")
        result = []
        req = request.args.get('touchpoint')
        for tp in search:
            if req == tp['touchpoint']:
                result.append(tp)
    else:
        result = search

    resp = {}
    resp["status"]=200
    resp["result"]= result
    return jsonify(resp)


@app.route('/health')
def hello():
    return jsonify({"status":"ok"})


