import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
try:
    client.admin.command('ismaster')
    print("Connected to the database successfully.")

except Exception as e:
    print(f"Could not connect to the database: {e}")

db = client["service_provider"]
service_provider = db["services_data"]

