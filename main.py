import urllib.request
import requests

#opener = urllib.build_opener()

#response = opener .open ("https://httpbin.org/get")

#print(response.read()



#res = requests.post ("https://httpbin.org/post", data-"Test data hello world", headers-("hi": "My title"})
#print(res.text)



#response = requests. get ("https: //httpbin.org/get")
#print (response.content)

coin_list = []

response = requests.get("https://coinmarketcap.com/")
#print(response.text)
response_text = response.text

response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if parse_elem1.startswith("$"):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem1.startswith("$") and  parse_elem2[1].isdigit():
                coin_list.append(parse_elem2)

btc = coin_list[0]
print("BTC =", btc)