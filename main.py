from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('create_event.html')

@app.route("/graph")
def second_page():
	return render_template('graph.html')

if __name__ == "__main__":
    app.run()