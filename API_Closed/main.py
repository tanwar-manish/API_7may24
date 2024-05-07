import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
	"X-RapidAPI-Key": "8b26551330msh2db9d5f18688bebp156d4djsn85d2b872776b",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

querystring = {"q":"20,-0.13"}

response = requests.get(url, headers=headers, params=querystring)
print(response.json())     ### dictionary object

# print(type(response.content))   ### bytes object

# import json

# data = json.dumps(response.json())
# print(type(data))

### loads method - convert JSON string to dictinary





