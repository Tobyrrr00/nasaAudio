import requests
import json
import webbrowser

with open("..\\api_key.txt", "r") as file:
    key = file.read().strip()

url = 'https://api.nasa.gov/planetary/apod'

params = {
    'api_key' : key,
    'hd' : 'true',
}

response = requests.get(url=url, params=params)
json_data = response.json()
image_url = json_data['hdurl']
webbrowser.open(image_url)