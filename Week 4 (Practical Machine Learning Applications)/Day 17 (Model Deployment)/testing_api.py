#Calling api and testing it
import requests

#urls = http://127.0.0.1:8000/predict for localhost http://192.168.1.124:4444 for mac ID of the computer
# url = "http://127.0.0.1:4444/predict"

#For FastAPI
url = "http://127.0.0.1:8000/predict"
data = {'features': [5.1, 3.5, 1.4, 0.2]}
# data = {'features' : [6.1, 6.5, 3.4,5.2]}
response = requests.post(url, json=data)
print(response.json())

