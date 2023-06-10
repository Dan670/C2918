import urllib.request
import requests

response = requests.get("https://coinmarketcap.com/")
response_text = response.text

coin_list = []

response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if parse_elem1.startswith("$"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith("$") and parse_elem2[1].isdigit():
                coin_list.append(parse_elem2)

a = coin_list[0]
b = coin_list[1]
c = coin_list[2]
d = coin_list[3]
e= coin_list[4]
f = coin_list[5]
g = coin_list[6]
h = coin_list[7]
i = coin_list[8]
j = coin_list[9]


print('TOP1 =', a)
print('TOP2 =', b)
print('TOP3 =', c)
print('TOP4 =', d)
print('TOP5 =', e)
print('TOP6 =', f)
print('TOP7 =', g)
print('TOP8 =', h)
print('TOP9 =', i)
print('TOP10 =', j)



