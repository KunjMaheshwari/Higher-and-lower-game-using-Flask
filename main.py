from flask import Flask, render_template
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src='https://media.giphy.com/media/Rs2QPsshsFI9zeT4Kn/giphy.gif' style='width:400px;height:400px;'>"



@app.route('/<int:guess>')
def guess_number(guess):
    if(guess<random_number):
        return "<h1 style='color: red'>It's too low</h1>\
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' style='width:400px;height:400px;'>"
    elif(guess>random_number):
        return "<h1 style='color: red'>It's too high</h1>\
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style='width:400px;height:400px;'>"
    else:
        return "<h1 style='color: green'>CONGRATULATIONS</h1>\
            <h2 style='color: green'>You found the correct number</h2>\
                <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style='width:400px;height:400px;'>"
    





if __name__ == "__main__":
    app.run(debug=True)