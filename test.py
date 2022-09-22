import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb://localhost:27017")
df = pd.read_csv(
    "names.csv")
data = df.to_dict(orient="records")
db = client["dummydata"]
print(db)
db.empDetails.insert_many(data)
