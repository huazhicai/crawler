import requests
import time

start = time.time()
response = requests.get('http://python.org')
print(response.text)
end = time.time()
print(end-start)