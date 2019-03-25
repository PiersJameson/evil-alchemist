from flask import Flask, render_template, request, redirect
from math import sqrt
from prime import divisors

app = Flask(__name__)

#Create the main route or pass POSTs onto the number facts route
@app.route('/', methods=["GET", "POST"])
def hello():
    
    # POST requests should respond with number facts
    if request.method == "POST":
        number = request.form["number"]
        url = "".join(["/", str(number)])
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

if __name__ == '__main__':
    app.run()