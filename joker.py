import requests
import json


def jokes(f):

    data = requests.get(f)
    tt = json.loads(data.text)
    return tt


f = r"https://official-joke-api.appspot.com/jokes/programming/random"
a = jokes(f)

for i in (a):
    print(i["type"])
    print(i["setup"])
    print(i["punchline"], "\n")
