# Import Module
import os
import json
from operator import itemgetter

src_d = os.getcwd()

provinces_d = os.path.join("","/home/huydq/ITSS Linux/CovidTracking//provinces")

vaccine_json = os.path.join(provinces_d,"vaccine.json")
province_json = os.path.join(provinces_d,"province.json")
dose_json = os.path.join(provinces_d,"dose.json")
case_json = os.path.join(provinces_d,"case.json")
case_by_day_json = os.path.join(provinces_d,"caseByDay.json")
death_by_day_json = os.path.join(provinces_d,"deathByDay.json")

with open(dose_json,"r") as file:
    doses = json.load(file)

with open(vaccine_json,"r") as file:
    vaccines = json.load(file)

with open(province_json,"r") as file:
    provinces = json.load(file)

with open(case_json,"r") as file:
    cases = json.load(file)

with open(case_by_day_json,"r") as file:
    case_by_day = json.load(file)

with open(death_by_day_json,"r") as file:
    death_by_day = json.load(file)

ONE_MILLION = 1000000
ONE_THOUSAND = 1000
province_vaccinated_population = 0
province_two_dose_population = 0

def times_million(str):
    str = str.replace("M","")
    str = str.replace(",",".")
    str = float(str)
    str *= ONE_MILLION
    return str
def times_thousand(str):
    str = str.replace("K","")
    str = str.replace(",",".")
    str = float(str)
    str *= ONE_THOUSAND
    return str

for province in vaccines:
    province["province_two_dose_percentage"] = province["province_two_dose_percentage"].replace("%","")
    province["province_two_dose_percentage"] = float(province["province_two_dose_percentage"].replace(",","."))
    if "M" in province["province_vaccinated_population"]:
        province["province_vaccinated_population"] = times_million(province["province_vaccinated_population"])
    else:
        province["province_vaccinated_population"] = times_thousand(province["province_vaccinated_population"])
    if "M" in province["province_two_dose_population"]:
        province["province_two_dose_population"] = times_million(province["province_two_dose_population"])
    else:
        province["province_two_dose_population"] = times_thousand(province["province_two_dose_population"])
    province_vaccinated_population += province["province_vaccinated_population"]
    province_two_dose_population += province["province_two_dose_population"]
province_one_dose_population = province_vaccinated_population - province_two_dose_population

COUNTRY_POPULATION = 98*ONE_MILLION
list = [{
    "vaccinated_population":str(round(province_vaccinated_population/ONE_MILLION))+"M",
    "vaccinated_percentage":str(round(province_vaccinated_population/COUNTRY_POPULATION*100))+ "% population"
},{
    "two_dose_population":str(round(province_two_dose_population/ONE_MILLION))+"M",
    "two_dose_percentage":str(round(province_two_dose_population/COUNTRY_POPULATION*100))+"% population"
},
{
    "one_dose_population":str(round(province_one_dose_population/ONE_MILLION))+"M",
    "one_dose_percentage":str(round(province_one_dose_population/COUNTRY_POPULATION*100))+"% population"
}
]


sorted_provinces = sorted(vaccines,  key=itemgetter('province_two_dose_percentage'),reverse=True)
top_vaccinated_provinces = sorted_provinces[0:10]
least_vaccinated_provinces = sorted_provinces[53:63]






