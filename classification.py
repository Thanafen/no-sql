import numpy as np
import pandas as pd
from pymongo import MongoClient

#Connect to MongoDBAtlas

#Start with the connection to the cluster inside the MongoDBAtlas
client = MongoClient("mongodb://<Thanafen>:<passcode134>@ac-0vlxv8o-shard-00-00.dfjhj0f.mongodb.net:27017,ac-0vlxv8o-shard-00-01.dfjhj0f.mongodb.net:27017,ac-0vlxv8o-shard-00-02.dfjhj0f.mongodb.net:27017/?ssl=true&replicaSet=atlas-12gd2i-shard-0&authSource=admin&appName=Cluster0")

# Select the database
db = client["analytics"] #database
collection = db["clickstream"] #inside the database

# Retrieve documents
data = list(collection.find())

df= pd.DataFrame(data)

print(df.head())