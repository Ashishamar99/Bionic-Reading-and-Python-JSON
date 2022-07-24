# https://bible-api.com/1%20chronicles%2011?translation=bbe&verse_numbers=true
# https://bionic-reading.com/
import requests
import data

url = "https://ajith-holy-bible.p.rapidapi.com/GetBooks"
holyBibleHeaders = data.holyBibleHeaders
response = requests.request("GET", url, headers=holyBibleHeaders)

print(response.text)