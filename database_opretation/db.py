import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["APIS_testing"]
cryptocurrency = mydb['cryptocurrency_prices']

def get_data(data):
    if data['filter'] == 'all':
        result = list(cryptocurrency.find({},{"_id":0}))
    else:
        if data['type'] == 'top':
            result = list(cryptocurrency.find({},{"_id":0}).sort({'rank':1}))
        else:
            result = list(cryptocurrency.find({},{"_id":0}).sort({'rank':-1}))
    return result

def put_data(data):
    cryptocurrency.update_one({'name':data['name']},{"$set":data})
    return True

def post_data(data):
    result = cryptocurrency.find_one({"name":data['name']},{"_id":0})
    if result != None:
        cryptocurrency.insert_one(data)
    else:
        cryptocurrency.insert_one(data)
