import json
import csv

density = {}
with open('mat-do-dan-so.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        # check to skip the header row
        if row[0] != ' ':
            density[row[0]] = float(row[1])
with open('vn-projected.json') as f:
    geo = json.load(f)
geo_provinces = set(f['properties']['ten_tinh'] for f in geo['features'])
density_provinces = set(density.keys())
geo_provinces - density_provinces
corrections = {
    'Bà Rịa -Vũng Tàu': 'Bà Rịa - Vũng Tàu',
    'Cần Thơn': 'Cần Thơ',
    'Hòa Bình': 'Hoà Bình',
    'Khánh Hòa': 'Khánh Hoà',
    'Kien Giang': 'Kiên Giang',
    'Quản Bình': 'Quảng Bình',
    'TP. Hồ Chí Minh': 'TP.Hồ Chí Minh',
    'Thanh Hóa': 'Thanh Hoá',
    'Đăk Lăk': 'Đắk Lắk',
    'Đăk Nông': 'Đắk Nông'
}

for feature in geo['features']:
    name = feature['properties']['ten_tinh']
    if name in corrections:
        # correct province's name if needed
        feature['properties']['ten_tinh'] = corrections[name]
        name = corrections[name]

    # add density property and remove unused others
    feature['properties']['density'] = density[name]
    del feature['properties']['gid']
    del feature['properties']['code']

# and let's see if we still seeing any differences
geo_provinces = set(f['properties']['ten_tinh'] for f in geo['features'])
geo_provinces - density_provinces
with open('vn-density.json', 'w') as f:
    json.dump(geo, f)

