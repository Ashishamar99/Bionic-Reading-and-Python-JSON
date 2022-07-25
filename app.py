# https://bible-api.com/1%20chronicles%2011?translation=bbe&verse_numbers=true
# https://bionic-reading.com/
import requests
import data
import json
from functions import *

url = "https://ajith-holy-bible.p.rapidapi.com/GetBooks"
holyBibleHeaders = data.holyBibleHeaders
responseObject = requests.request("GET", url, headers=holyBibleHeaders)
response = responseObject.text
jsonData = json.loads(response)

oldTestament, newTestament = getBooksFromDictionary(jsonData)