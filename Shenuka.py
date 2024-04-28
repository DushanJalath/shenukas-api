
from fastapi import FastAPI,HTTPException
from models import Item,User
from typing import List
from pymongo import MongoClient
import numpy as np

client = MongoClient('mongodb+srv://dushanprabash:RIm0P0lBP8n2Jb7h@shenukacluster.cjwoari.mongodb.net/')

db = client['grocery']  
winter_collection = db['winter_items'] 
summer_collection = db['summer_items'] 
spring_collection = db['spring_items'] 
fall_collection = db['fall_items'] 
user_collection=db['user']

app=FastAPI()

@app.get('/')
async def initialReq():
    return {"Hello":"World"}
    
@app.post('/login')
async def login(user: User):
    res_user =await user_collection.find_one({"username": user.username})
    if not res_user or not user.password == res_user["password"]:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return res_user


@app.post('/getItems')
async def getItems(items: List[Item],season: str):
    lenght=len(items)
    couples = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            couples.append((items[i].item+" : "+items[j].item))
    if season=="Winter":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = winter_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1],reverse=True))
    if season=="Summer":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = summer_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1],reverse=True))
    if season=="Spring":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = spring_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1],reverse=True))
    if season=="Fall":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = fall_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1],reverse=True))
    prod_set=[]
    for key,val in sorted_results.items():
        key_split=key.split(" : ")
        if key_split[0] not in prod_set :
            prod_set.append(key_split[0])
        if key_split[1] not in prod_set:
            prod_set.append(key_split[1])
        
    return prod_set
    

