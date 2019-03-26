from flask import Flask, render_template, request, redirect
from math import sqrt
from prime import divisors
from flask_sqlalchemy import SQLAlchemy
import string

# Instantiate a flask app
app = Flask(__name__)

# Configure and instantiate MYSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://piersjameson:My MySQL pass.@piersjameson.mysql.pythonanywhere-services.com/piersjameson$default'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



#Create the main route or pass POSTs onto the number facts route
@app.route('/', methods=["GET", "POST"])
def hello():
    
    # POST requests should respond with number facts
    if request.method == "POST":
        number = list(request.form["number"])

        # Strip out anything that's not an integer number
        strippedNumber = [n for n in number if str(string.digits.find(n)) == n]
        strippedNumber = "".join(strippedNumber)

        # Redirect to url created from sanitized, strippedNumber
        url = "".join(["/", strippedNumber])
        return redirect(url)
    
    # GET requests should respond with the index page
    return render_template("index.html")


# Number facts route
@app.route('/<int:number>')
def numberReturn(number):

    # Create a warning to be passed along if submitted number is out of bounds
    warning = ""
    if number > 1000000 or number < 0:
        number = 1
        warning = "Warning! Only numbers between 1 and 1000000 please"
    
    # Create a list of divisors to determine primality and pass along for display
    divisorList = divisors(number)

    # Create a message to pass along regarding primality
    primeMessage = " is PRIME!"
    if len(divisorList) != 2:
        primeMessage = " is NOT prime!"
    
    #Determine the Square Root to pass along for display
    root = "{:.4f}".format(sqrt(number))

    # Render the page, passing along number, divisorList, root, warning, and primality message.
    return render_template("number.html",number=number,divisorList=divisorList,root=root,primeMessage=primeMessage,warning=warning)

# Handle a string being submitted instead of a number
@app.route('/string:urlString')
def stringHandler():
    return redirect("/")



if __name__ == '__main__':
    app.run()