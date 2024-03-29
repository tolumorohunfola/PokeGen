# importing the flask class and the render template function
from flask import Flask, render_template
# importing the get_poke_info function from the information about pokemons file
from information_about_pokemons import get_poke_info

# defining the flask app as an instance of the flask class
app = Flask(__name__)

@app.route("/")  # the slash means that when we go to the default page, the function is run
def home():  # this line defines each page's function
    return render_template('mainPage.html') #this tells the app to use the code in the mainPage.html file

# when /random is added to the default url, the random pokemon page is run
@app.route('/random')
def randomPokemon():
    # defines the variables needed for the page to run using the get_poke_info function
    name, sprite, weight, height, ability, poke_type = get_poke_info(0,300)
    # renders the random_pokemon page with the variables defined above linked to the page's variables
    return render_template('random_pokemon.html', img_url=sprite, name=name, weight=weight, height=height, ability=ability, poke_type=poke_type)

# when /my-pokemon is added to the default url, the my pokemon page is run
@app.route("/my-pokemon")
def my_pokemon():
    # renders the html for the my pokemon page
    return render_template('my_pokemon.html')

# when /Poke-info is added to the default url, the poke-info page is run
@app.route("/Poke-info")
def poke_info():
    # defines the variables needed for the page to run using the get_poke_info function
    name0, sprite0, weight0, height0, ability0, poke_type0 = get_poke_info(0,300)
    name1, sprite1, weight1, height1, ability1, poke_type1 = get_poke_info(0,300)
    name2, sprite2, weight2, height2, ability2, poke_type2 = get_poke_info(0,300)
    name3, sprite3, weight3, height3, ability3, poke_type3 = get_poke_info(0,300)
    name4, sprite4, weight4, height4, ability4, poke_type4 = get_poke_info(0,300)
    name5, sprite5, weight5, height5, ability5, poke_type5 = get_poke_info(0,300)
    # renders the pokemon info page with the variables defined above linked to the page's variables
    return render_template('PokemonInfoTemplate.html',
    img_url0=sprite0, name0 =name0, weight0=weight0, height0=height0, ability0=ability0, poke_type0=poke_type0,
    img_url1=sprite1, name1 =name1, weight1=weight1, height1=height1, ability1=ability1, poke_type1=poke_type1,
    img_url2=sprite2, name2 =name2, weight2=weight2, height2=height2, ability2=ability2, poke_type2=poke_type2,
    img_url3=sprite3, name3 =name3, weight3=weight3, height3=height3, ability3=ability3, poke_type3=poke_type3,
    img_url4=sprite4, name4 =name4, weight4=weight4, height4=height4, ability4=ability4, poke_type4=poke_type4,
    img_url5=sprite5, name5 =name5, weight5=weight5, height5=height5, ability5=ability5, poke_type5=poke_type5,)

# runs the application
if __name__ == "__main__":
    app.run()