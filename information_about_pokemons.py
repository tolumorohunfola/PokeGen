
import pip._vendor.requests  #this allows us to import this module to make requests in the api
import requests
import random
from pprint import pprint #pprint means pretty print -very useful for apis :)
def get_poke_info():
    random_number = random.randint(0, 100)
    # print(random_number) I used this to check that the random number was correctly generated but no need anymore
    pokemon_page = "https://pokeapi.co/api/v2/pokemon/{}/".format(random_number)
    # print(pokemon_page) I used this to check that the formatting worked but no need anymore
    response = requests.get(pokemon_page)
    status = response.status_code #tells us how running the code went
    # print(response.text) # I need to figure out what this means
    # print(response)
    pokemon = response.json()
    pprint(pokemon) #not sure if needed
    name = pokemon['name']
    sprite = pokemon['sprites']['front_default']
    weight = pokemon['weight']
    height = pokemon['height']
    # moves = pokemon['moves'] #I need to learn how to do this properly - we need to programme a random function for 4 unique moves and then put this on the page as well
    return(name, sprite, weight, height)

# print(name) #need to figure out this not working
# print(sprite)
# print(weight)
# print(height)


# our api is going to be https://pokeapi.co/
