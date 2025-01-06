import requests

response = requests.get("https://api.chucknorris.io/jokes/random?category=dev")

print(response.text)
