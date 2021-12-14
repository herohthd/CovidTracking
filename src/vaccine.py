# Import Module
import os
import json

src_d = os.getcwd()

provinces_d = os.path.join("","/home/huydq/Projects/CovidTracking/provinces")
print(provinces_d)
vaccine_json = os.path.join(provinces_d,"vaccine.json")
province_json = os.path.join(provinces_d,"province.json")

print(vaccine_json)

with open(vaccine_json,"r") as file:
    vaccines = json.load(file)

with open(province_json,"r") as file:
    provinces = json.load(file)

one_million = 1000000
one_thousand = 1000
province_vaccinated_population = 0
province_two_dose_population = 0
province_population = 0

def times_million(str):
    str = str.replace("M","")
    str = str.replace(",",".")
    str = float(str)
    str *= one_million
    return str
def times_thousand(str):
    str = str.replace("K","")
    str = str.replace(",",".")
    str = float(str)
    str *= one_thousand
    return str

for province in vaccines:
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

province_population = 98*one_million
list = [{
    "vaccinated_population":str(round(province_vaccinated_population/one_million))+"M",
    "vaccinated_percentage":str(round(province_vaccinated_population/province_population*100))+ "% population"
},{
    "two_dose_population":str(round(province_two_dose_population/one_million))+"M",
    "two_dose_percentage":str(round(province_two_dose_population/province_population*100))+"% population"
},
{
    "one_dose_population":str(round(province_one_dose_population/one_million))+"M",
    "one_dose_percentage":str(round(province_one_dose_population/province_population*100))+"% population"
}
]
print(list)






