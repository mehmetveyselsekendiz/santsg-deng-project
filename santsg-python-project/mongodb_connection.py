import pymongo
from get_dataset import forbes_billionaires_list

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_mongo_db = my_client["santsg-db"]
my_collection = my_mongo_db["forbes-billionaires"]

# Run the code below to insert dataset to mongodb
# my_collection.insert_many(forbes_billionaires_list)