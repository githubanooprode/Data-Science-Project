from flask import Flask
app = Flask(__name__)


@app.route('/how r u')
def hello():
    return "im fine"

@app.route('/where r u')
def whre():
    return "im here"

if __name__ == "__main__":
    app.run()



