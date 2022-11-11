import requests, random

def generateRandomFact():
    animal = random.randint(1, 2)

    if animal == 1:
        res = requests.get('https://dog-api.kinduff.com/api/facts')
        json = res.json()
        string = str(json['facts'])
        nstring = string.replace('[', '')
        return nstring.replace(']', '')
    elif animal == 2:
        res = requests.get('https://catfact.ninja/fact?max_length=140')
        json = res.json()
        return json['fact']