
from fastapi import FastAPI
import pandas as pd
import numpy as np
from models import Item
from typing import List


app=FastAPI()

# data=pd.read_csv("E:\\Freelance Assignments\\Shenuka - IIT\\Retail_Transactions_Dataset.csv")

# product_array=data["Product"].to_numpy()

# product_set=[]
# for product_row in product_array:
#     output_array=eval(product_row)
#     product_set.append(output_array)
    
# #print(product_set)

# flat_product_list=[item for sublist in product_set for item in sublist]
# flat_product_list

# unique_product_list=np.unique(flat_product_list)
# #print(len(unique_product_list))
# print(unique_product_list)


# selling_map = {}

# for i in range(len(unique_product_list)):
#     for j in range(i + 1, len(unique_product_list)):
#         a = unique_product_list[i]
#         b = unique_product_list[j]
#         count = 0
#         for item_set in product_set:
#             if a in item_set and b in item_set:
#                 count += 1
#         e = a + " : " + b
#         selling_map[e] = count 

# #print(selling_map)

# sorted_selling_map = sorted(selling_map.items(), key=lambda x: x[1])
# #print(sorted_selling_map)

@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.get('/getItems')
async def save_bill_details(items: List[Item]):
    for item in items:
        # Concatenate the string representation of each item
        items_string += f"{item.name} "
    return items_string
