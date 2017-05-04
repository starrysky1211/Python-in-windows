import json

data = open('city.txt')
cities = data.read()
data.close()
cities_list = cities.split(',')
cities_dict = {}
for h in cities_list:
    city = h.split('|')
    cities_dict[city[1]] = city[0]
cities_json = json.dumps(cities_dict, ensure_ascii=False, indent=4)

new = open('city_dict.txt', 'w')
new.write(cities_json)
new.close()
