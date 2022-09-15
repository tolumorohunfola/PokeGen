from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('mainPage.html')
# put a button in here to lead to different pages

@app.route("/view-my-pokemon")
def view_pokemon():
    return "This is your pokemons :)"

if __name__ == "__main__":
    app.run()