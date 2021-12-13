# Import Module
import os
import json

src_d = os.getcwd()

provinces_d = os.path.join(src_d,"../provinces")

province_json = os.path.join(provinces_d,"province.json")

with open(province_json,"r") as file:
    provinces = json.load(file)
    print(provinces[10]["province_name"])

