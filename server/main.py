from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/second_page")
def second_page():
	return "you are at second page"

if __name__ == "__main__":
    app.run()