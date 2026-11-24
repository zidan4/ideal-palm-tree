import requests

r = requests.get('https://httpbin.org/get')
print(r.status_code)
print(r.text)

#with open('response.txt', 'w') as f:
 # f.write(r.text)

print(r.json())
print(r.headers)
print(r.ok)