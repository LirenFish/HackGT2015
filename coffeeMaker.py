from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/Roast', methods = ['GET','POST'])
def roast():
    print "inside Roast"
    return render_template("Roast.html")

@app.route('/Brew', methods = ['GET','POST'])
def brew():
    if request.method == 'POST':
        first_name = request.form["firstname"]
        brew_type = request.form["roastType"]
        print (brew_type)
        print 789
        return render_template("Brew.html",selection = brew_type, name = first_name)
    else:
        return "This is a GET request."
    


if __name__ == '__main__':
    app.run()
