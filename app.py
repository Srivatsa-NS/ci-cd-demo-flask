from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "CI/CD Pipeline Demo is Live!"


if __name__ == "__main__":
    app.run(debug=True)
