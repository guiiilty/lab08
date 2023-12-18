import requests

def apirequestclosure(url):
    def makeapirequest():
        response = requests.get(url)
        if response.statuscode == 200:
            return response.text
        else:
            return None
    return makeapirequest

dogfactapi = apirequestclosure('https://dogapi.dog/api/v2/facts')
dogfact = dogfactapi()
print(dogfact)