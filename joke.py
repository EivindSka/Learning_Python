from jokeapi import Jokes  # Import the Jokes class
import asyncio


async def print_joke():
    j = await Jokes()  # Initialise the class
    await j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single":  # Print the joke
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])

asyncio.run(print_joke())
