import requests

url = "https://icanhazdadjoke.com"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print("This is just a joke \n" + response.text)
