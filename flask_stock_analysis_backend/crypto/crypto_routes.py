import requests
from flask import Blueprint, request, jsonify
from . import  fetch_crypto_data


crypto_blues = Blueprint('crypto_blues', __name__)


@crypto_blues.route("/", methods=["GET", "POST"])
def crypto_home():
    if request.method == "GET":
        return jsonify({"route": 'Main crypto Blueprint', "method": "GET"}), 200

    if request.method == "POST":
        return jsonify({"route": '---- Main crypto Blueprint ------', "method": "POST"}), 200


@crypto_blues.route("/crypto_data", methods=["POST"])
def crypto_data():
    if request.method == "POST":
        return jsonify({"route": "crypto_data", "method": "POST"})

@crypto_blues.route("/get_crypto_data", methods=["GET"])
def get_crypto_data():
    if request.method == "GET":
        data = {
            'filter' : 'filter' ,
            'limit': 5,
            'type':  'low',#'top' 
        }
        # data = {
        #     'filter' : 'all', 
        #     'limit': 3,
        #     'type': 'top' 
        # }
        result = fetch_crypto_data.get_data(data)
        return jsonify({"route": "get_crypto_data", "method": "POST",'data':result})


@crypto_blues.route("/updated_crypto_data", methods=["GET"])
def updated_crypto_data():
    if request.method == "GET":
        endpoint = "https://api.coincap.io/v2/assets"
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        response = requests.get(endpoint, headers=headers)
        for i in range(len(response.json()["data"])):
            fetch_crypto_data.post_data(response.json()["data"][i])
        return jsonify({"route": "updated_crypto_data", "method": "GET", "Status" : "updated "}), 200