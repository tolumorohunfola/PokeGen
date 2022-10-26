from flask import Flask, render_template
from information_about_pokemons import get_poke_info

app = Flask(__name__)

@app.route("/")  # the slash means that when we go to the default page, the below is displayed
def home():  # this line defines each page's function - very useful
    return render_template('mainPage.html') #this means tells the app to use the code in the html file
# put a button in here to lead to different pages

@app.route('/random')
def  randomPokemon():
    return render_template('random_pokemon.html')


@app.route("/my-pokemon")
def my_pokemon():
    return render_template('my_pokemon.html')

@app.route("/Poke-info")
def poke_info():
    name0, sprite0, weight0, height0 = get_poke_info()
    name1, sprite1, weight1, height1 = get_poke_info()
    name2, sprite2, weight2, height2 = get_poke_info()
    name3, sprite3, weight3, height3 = get_poke_info()
    name4, sprite4, weight4, height4 = get_poke_info()
    name5, sprite5, weight5, height5 = get_poke_info()
    return render_template('PokemonInfoTemplate.html', img_url0=sprite0, name0 =name0, weight0=weight0, height0=height0, img_url1=sprite1, name1 =name1, weight1=weight1, height1=height1, img_url2=sprite2, name2 =name2, weight2=weight2, height2=height2, img_url3=sprite3, name3 =name3, weight3=weight3, height3=height3, img_url4=sprite4, name4 =name4, weight4=weight4, height4=height4, img_url5=sprite5, name5 =name5, weight5=weight5, height5=height5)


if __name__ == "__main__":
    app.run()