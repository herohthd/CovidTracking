# Import Module
import os
import json
from operator import itemgetter

src_d = os.getcwd()

provinces_d = os.path.join("","/home/huydq/ITSS Linux/CovidTracking//provinces")

case_json = os.path.join(provinces_d,"case.json")
case_by_day_json = os.path.join(provinces_d,"caseByDay.json")
death_by_day_json = os.path.join(provinces_d,"deathByDay.json")

with open(case_json,"r") as file:
    cases = json.load(file)

with open(case_by_day_json,"r") as file:
    case_by_day = json.load(file)

with open(death_by_day_json,"r") as file:
    death_by_day = json.load(file)








