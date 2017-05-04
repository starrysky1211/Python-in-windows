import urllib2
import json
import codecs

city_data = open('city_dict.txt')
cities_str = city_data.read()
city_data.close()
cities_dict = json.loads(cities_str)
true_dict = {}
for h in cities_dict:
    city_id = cities_dict[h]
    url = 'http://m.weather.com.cn/data5/city%s.xml' % city_id
    web = urllib2.urlopen(url)
    content = web.read()
    content_list = content.split(',')
    for h1 in content_list:
        city = h1.split('|')
        true_dict[city[1]] = '101'+city_id+city[0]

cities_json = json.dumps(true_dict)

with codecs.open('true_dict.txt', 'w', 'utf-8') as new:
    new.write(cities_json)
    new.close()

