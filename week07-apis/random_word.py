import requests

response = requests.get("https://random-word-api.herokuapp.com/word")

data = response.json()

word = data[0]

print(word)