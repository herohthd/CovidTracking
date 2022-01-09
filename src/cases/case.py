# Import Module
import os
import json
from operator import itemgetter

src_d = os.getcwd()

provinces_d = os.path.join("","/home/huydq/ITSS Linux/CovidTracking//provinces")

case_json = os.path.join(provinces_d,"case.json")
case_by_day_json = os.path.join(provinces_d,"caseByDay.json")
death_by_day_json = os.path.join(provinces_d,"deathByDay.json")
case_province_json = os.path.join(provinces_d,"caseProvince.json")

with open(case_json,"r") as file:
    cases = json.load(file)

with open(case_by_day_json,"r") as file:
    case_by_day = json.load(file)

with open(death_by_day_json,"r") as file:
    death_by_day = json.load(file)

with open(case_province_json,"r") as file:
    case_province = json.load(file)

for province in case_province:
    province['case'] = int(province['case'].replace(".",""))
sorted_provinces = sorted(case_province,  key=itemgetter('case'),reverse=True)
top_case_provinces = sorted_provinces[0:10]
least_case_provinces = sorted_provinces[53:63]




