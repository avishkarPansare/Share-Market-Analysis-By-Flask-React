import requests
import database_opreations 

endpoint = "https://api.coincap.io/v2/assets"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

def post_data():
    response = requests.get(endpoint, headers=headers)
    for i in range(len(response.json()["data"])):
        database_opreations.post_data(response.json()["data"][i])


def get_data_with_filter(data):
    # data = {
    #     'filter' : filter 
    #     'limit' 5,
    #     'type': 'top', # low 
    # }
    # data = {
    #     'filter' : all, 
    #     'limit' 0,
    #     'type': '' 
    # }
    result = database_opreations.get_data(data)
    return result

def log_data():
    pass



