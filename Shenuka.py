
from fastapi import FastAPI,HTTPException
from models import Item,User
from typing import List
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['grocery']  
winter_collection = db['winter_items'] 
summer_collection = db['summer_items'] 
spring_collection = db['spring_items'] 
fall_collection = db['fall_items'] 
user_collection=db['user']

app=FastAPI()

@app.get('/logIn')
async def login(user:User):
    user = user_collection.find_one({"username": user.username})
    if not user or not user.password==user["password"]:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user

@app.post('/getItems')
async def getItems(items: List[Item],season: str):
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
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
    if season=="Summere":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = summer_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
    if season=="Spring":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = spring_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
    if season=="Spring":
        results={}
        for couple in couples:
            search_query = {"Items": couple}
            result_doc = spring_collection.find_one(search_query)
            if result_doc:
                results[couple]=result_doc["count"]
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
    return sorted_results
    

