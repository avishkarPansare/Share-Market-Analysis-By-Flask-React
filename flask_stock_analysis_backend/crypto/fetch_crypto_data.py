import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["APIS_testing"]
cryptocurrency = mydb['cryptocurrency_prices']


def post_data(data):
    result = cryptocurrency.find_one({"name":data['name']},{"_id":0})
    if result != None:
        cryptocurrency.insert_one(data)
    else:
        cryptocurrency.insert_one(data)

def get_data(data):
    if data['filter'] == 'all':
        result = cryptocurrency.find({},{"_id":0}).limit(data['limit'])
    else:
        if data['type'] == 'top':
            result = cryptocurrency.find({},{"_id":0})
            result = result.sort("rank", pymongo.ASCENDING)
            result = list(result.limit(data['limit']))
        else:
            result = cryptocurrency.find({},{"_id":0})
            result = result.sort("rank", pymongo.DESCENDING)
            result = list(result.limit(data['limit']))
    return result