# API KEY DOCUMENTATION
# https://rapidapi.com/kaushiksheel9/api/pizza-and-desserts/
import requests

url = "https://pizza-and-desserts.p.rapidapi.com/pizzas/1"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "pizza-and-desserts.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())