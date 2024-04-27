import pandas as pd
import numpy as np
from pymongo import MongoClient



client = MongoClient('mongodb+srv://dushanprabash:RIm0P0lBP8n2Jb7h@shenukacluster.cjwoari.mongodb.net/')

db = client['grocery']  
winter_collection = db['winter_items'] 
summer_collection = db['summer_items'] 
spring_collection = db['spring_items'] 
fall_collection = db['fall_items'] 


data=pd.read_csv("E:\\Freelance Assignments\\Shenuka - IIT\\Retail_Transactions_Dataset.csv")

season_grouped_products = data.groupby("Season")["Product"]

winter_products = []
spring_products = []
summer_products = []
fall_products = []

# Iterate over the grouped products
for season, products in season_grouped_products:
    if season == 'Winter':
        winter_products.extend(products.tolist())
    elif season == 'Spring':
        spring_products.extend(products.tolist())
    elif season == 'Summer':
        summer_products.extend(products.tolist())
    elif season == 'Fall':
        fall_products.extend(products.tolist())

winter_product_set=[]
for product_row in winter_products:
    output_array=eval(product_row)
    winter_product_set.append(output_array)
    
spring_product_set=[]
for product_row in spring_products:
    output_array=eval(product_row)
    spring_product_set.append(output_array)
    

summer_product_set=[]
for product_row in summer_products:
    output_array=eval(product_row)
    summer_product_set.append(output_array)
    

fall_product_set=[]
for product_row in fall_products:
    output_array=eval(product_row)
    fall_product_set.append(output_array)

winter_flat_product_list=[item for sublist in winter_product_set for item in sublist]

spring_flat_product_list=[item for sublist in spring_product_set for item in sublist]

summer_flat_product_list=[item for sublist in summer_product_set for item in sublist]

fall_flat_product_list=[item for sublist in fall_product_set for item in sublist]



winter_unique_product_list=np.unique(winter_flat_product_list)

spring_unique_product_list=np.unique(spring_flat_product_list)

summer_unique_product_list=np.unique(summer_flat_product_list)

fall_unique_product_list=np.unique(fall_flat_product_list)



winter_selling_map = {}
for i in range(len(winter_unique_product_list)):
    for j in range(i + 1, len(winter_unique_product_list)):
        a = winter_unique_product_list[i]
        b = winter_unique_product_list[j]
        count = 0
        for item_set in winter_product_set:
            if a in item_set and b in item_set:
                count += 1
        e = a + " : " + b
        winter_selling_map[e] = count       
winter_sorted_selling_map = sorted(winter_selling_map.items(), key=lambda x: x[1])
winter_sorted_selling_map_dict = {key: value for key, value in winter_sorted_selling_map}


spring_selling_map = {}
for i in range(len(spring_unique_product_list)):
    for j in range(i + 1, len(spring_unique_product_list)):
        a = spring_unique_product_list[i]
        b = spring_unique_product_list[j]
        count = 0
        for item_set in spring_product_set:
            if a in item_set and b in item_set:
                count += 1
        e = a + " : " + b
        spring_selling_map[e] = count       
spring_sorted_selling_map = sorted(spring_selling_map.items(), key=lambda x: x[1])
spring_sorted_selling_map_dict = {key: value for key, value in spring_sorted_selling_map}


summer_selling_map = {}
for i in range(len(summer_unique_product_list)):
    for j in range(i + 1, len(summer_unique_product_list)):
        a = summer_unique_product_list[i]
        b = summer_unique_product_list[j]
        count = 0
        for item_set in summer_product_set:
            if a in item_set and b in item_set:
                count += 1
        e = a + " : " + b
        summer_selling_map[e] = count    
summer_sorted_selling_map = sorted(summer_selling_map.items(), key=lambda x: x[1])
summer_sorted_selling_map_dict = {key: value for key, value in summer_sorted_selling_map}


fall_selling_map = {}
for i in range(len(fall_unique_product_list)):
    for j in range(i + 1, len(fall_unique_product_list)):
        a = fall_unique_product_list[i]
        b = fall_unique_product_list[j]
        count = 0
        for item_set in fall_product_set:
            if a in item_set and b in item_set:
                count += 1
        e = a + " : " + b
        fall_selling_map[e] = count
fall_sorted_selling_map = sorted(fall_selling_map.items(), key=lambda x: x[1])
fall_sorted_selling_map_dict = {key: value for key, value in fall_sorted_selling_map}

for key, value in winter_sorted_selling_map_dict.items():
    record = {"Items": key, "count": value}
    winter_collection.insert_one(record)

for key, value in spring_sorted_selling_map_dict.items():
    record = {"Items": key, "count": value}
    spring_collection.insert_one(record)

for key, value in summer_sorted_selling_map_dict.items():
    record = {"Items": key, "count": value}
    summer_collection.insert_one(record)

for key, value in fall_sorted_selling_map_dict.items():
    record = {"Items": key, "count": value}
    fall_collection.insert_one(record)