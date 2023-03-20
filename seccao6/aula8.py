import requests

#http ->80
#https -> 433
url = 'http://localhost:3333/'
response = requests.get(url)
#print(response.text)
print(response.json)