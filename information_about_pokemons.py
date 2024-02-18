
import pip._vendor.requests  # this allows us to import this module to make requests in the api
import requests
import random
# from pprint import pprint # pprint means pretty print -very useful for apis :)

def get_poke_info(lower_limit, upper_limit):
    random_number = random.randint(lower_limit, upper_limit)
    # print(random_number) # I used this to check that the random number was correctly generated but no need anymore
    pokemon_page = f"https://pokeapi.co/api/v2/pokemon/{random_number}/"
    # print(pokemon_page) # I used this to check that the formatting worked but no need anymore
    response = requests.get(pokemon_page)
    # status = response.status_code # tells us how running the code went
    # print(response.text) # I need to figure out what this means
    pokemon = response.json()
    # pprint(pokemon) # for printing the response
    name = pokemon['name']
    sprite = pokemon['sprites']['front_default']
    weight = pokemon['weight']
    height = pokemon['height']
    ability = pokemon['abilities'][0]['ability']['name']
    poke_type = pokemon['types'][0]['type']['name']
    # moves = pokemon['moves'] # I need to learn how to do this properly - we need to programme a random function for 4 unique moves and then put this on the page as well
    return(name.title(), sprite, weight, height, ability.title(), poke_type.title())

# our api is going to be https://pokeapi.co/
