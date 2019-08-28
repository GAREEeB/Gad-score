import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'step_count':2, 'calories_burned':9, 'hours_of_sleep':6})

print(r.json())
