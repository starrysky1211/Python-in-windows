import json

cities = open('city.txt')
city = cities.read()
cities.close()
city2 = city.split(',')

data = json.dumps(city2, 'city.txt', ensure_ascii=False, indent=4)
print data


