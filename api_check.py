from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_token = os.environ.get("api_read_key")

# API-endpoint
URL = "https://api.purpleair.com/v1/sensors"
  
  
# Defining a params dict for the parameters to be sent to the API
PARAMS = {
    'api_key': api_token,
    'fields': 'name, latitude, longitude'
}
  
# Sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# Extracting data in json format
data = r.json()
print(data)

# Boundary box (https://gist.github.com/graydon/11198540)
# US': ('United States', (-171.791110603, 18.91619, -66.96466, 71.3577635769)),