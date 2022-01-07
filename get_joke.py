import json
from urllib import request

# url = 'https://v2.jokeapi.dev/joke/Programming'
url = 'https://v2.jokeapi.dev/joke/Any'
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)


class Joke:

    def __init__(self, setup, delivery) -> None:
        self.setup = setup
        self.delivery = delivery

    def __str__(self) -> str:
        return f'setup {self.setup} delivery {self.delivery}'


jokes = []

for i in jsonData:
    setup = i["setup"]
    delivery = i["delivery"]
    joke = Joke(setup, delivery)
    jokes.append(joke)

for joke in jokes:
    print(joke)


# def PrintJoke:
#     if jsonData['type'] == 'single':
#         print(jsonData['joke'])
#     else:
#         print(jsonData['setup'])
#         print(jsonData['delivery'])
