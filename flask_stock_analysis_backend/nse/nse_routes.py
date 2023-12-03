import requests
from flask import Blueprint, request, jsonify

nse_blues = Blueprint('nse_blues', __name__)


@nse_blues.route("/", methods=["GET", "POST"])
def nse_home():
    if request.method == "GET":
        return jsonify({"route": 'Main NSE Blueprint', "method": "GET"}), 200

    if request.method == "POST":
        return jsonify({"route": '---- Main NSE Blueprint ------', "method": "POST"}), 200


@nse_blues.route("/nse_stock_data", methods=["POST"])
def nse_stock_data():
    if request.method == "POST":
        return jsonify({"route": "nse_stock_data", "method": "POST"})