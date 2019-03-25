from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    render_template("index.html")

@app.route('/numberstuff', methods=["POST"])
def numberStuff():
    number = request.form.get("number")
    return number

if __name__ == '__main__':
    app.run()