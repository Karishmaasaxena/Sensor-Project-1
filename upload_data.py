from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
uri="mongodb+srv://saxenakarishma48:karishma48@cluster0.b4bln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server
client=MongoClient(uri)

# create database name and collection name
DATABASE_NAME="mlproject"
COLLECTION_NAME="wafer fault"

df=pd.read_csv("notebooks\wafer_23012020_041211.csv")
df=df.drop(columns="Unnamed: 0",axis=1)
df.sample()

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)