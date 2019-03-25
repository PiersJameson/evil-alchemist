from flask import Flask, render_template, request
from math import sqrt
from prime import divisors

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/numberstuff', methods=["POST"])
def numberStuff():
    number = request.form.get("number")
    return number

@app.route('/<int:number>')
def numberReturn(number):
    primeMessage = " is PRIME!"
    divisorList = divisors(number)
    if len(divisorList) != 2:
        primeMessage = " is NOT prime!"
    root = sqrt(number)
    return render_template("number.html",number=number,divisorList=divisorList,root=root,primeMessage=primeMessage)

if __name__ == '__main__':
    app.run()