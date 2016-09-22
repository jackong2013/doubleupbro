from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/second_page")
def second_page():
	return "you are at second page"

if __name__ == "__main__":
    app.run()