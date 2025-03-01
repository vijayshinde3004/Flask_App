from flask import Flask


app = Flask(__name__)


@app.route("/vijay")  #portnumber

def home():
    return "This is Flask Application "


if __name__=="__main__":
    app.run(debug=True)