from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run()