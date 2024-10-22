import requests

url = "https://jokes-always.p.rapidapi.com/common"

headers = {
	"x-rapidapi-key": "744a48c97cmsh959f96c56a935ecp1209f4jsn124057d036b7",
	"x-rapidapi-host": "jokes-always.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
output=response.json()

print("Fetching a joke......")
print(f"Here is a joke: {output['data']}")
