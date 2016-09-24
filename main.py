from flask import Flask, render_template, request, redirect
import fitbit_pkg.fitbit as fitbit
import threading
import webbrowser
app = Flask(__name__)

FITBIT_CLIENT_ID = '227ZV2'
FITBIT_CLIENT_SECRET = 'fbce23292834b5f580ba9c24020d4397'
FITBIT_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0WTczWDkiLCJhdWQiOiIyMjdaVjIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNDc0NzE0MTQyLCJpYXQiOjE0NzQ2ODUzNDJ9.8Togz1TI95ssFt0cNge_Vy4-7Xv28_Tcl9vC6rJXtXU'
FITBIT_REFRESH_TOKEN = 'd782cf489f8d2214e9937e4d76931abe4ca035c0bc93fdbe3279560d058da7f8'

@app.route("/")
def hello():
    return render_template('create_event.html')

@app.route("/connect_fitbit")
def connect_fitbit():
	return render_template("connect_fitbit.html")

@app.route("/connect_attempt")
def connect_attempt():
	authd_client = fitbit.FitbitOauth2Client(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET)
	url, _ = authd_client.authorize_token_url(redirect_uri='http://127.0.0.1:5000/fatty')
	return redirect(url)

@app.route("/fatty")
def fatty_stats():
	return render_template('fatty.html')

@app.route("/commander")
def commander_view():
	return render_template('commander.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)