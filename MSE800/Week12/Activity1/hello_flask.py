from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hello Flask Page</title>
    </head>
    <body>
        <p>Hello Flask</p>
    </body>
    </html>
    """

@app.route("/bye")
def bye():
    return "<p>Bye Flask</p>"

@app.route("/username/<name>")
def greet(name):
    return f"{name}, is learing Flask!"

@app.route("/<name>/<int:number>")
def learn(name, number):
    return f"<p>{name}, is learing Flask! {number}.</p>"

@app.route("/resources")
def resource():
    return f"<p>Flask Resource <a href='https://flask.palletsprojects.com/en/stable/quickstart/#'>www.flask.palletsprojects.com</a></p>"


if __name__ == "__main__":
    app.run(debug=True)