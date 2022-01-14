import json
from urllib import request

url = 'https://v2.jokeapi.dev/joke/Programming'
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)
print(jsonData)


# This block of code will make sure to look thorugh the different values and print each of them individually to make sure it does not get missed
for key, value in jsonData.items():
    if key == 'joke':
        print(value)
    if key == 'setup':
        print(value)
    if key == 'delivery':
        print(value)
