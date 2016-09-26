from flask import Flask, render_template, request, redirect, url_for
import fitbit_pkg.fitbit as fitbit
import pprint as pp
import json
app = Flask(__name__)

FITBIT_CLIENT_ID = '227ZV2'
FITBIT_CLIENT_SECRET = 'fbce23292834b5f580ba9c24020d4397'
FITBIT_ACCESS_TOKEN = None
FITBIT_REFRESH_TOKEN = None
REDIRECT_URI = 'http://127.0.0.1:5000/receive_fitbit'
authd_client = fitbit.FitbitOauth2Client(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET)

@app.route("/")
def hello():
    return render_template('create_event.html')

@app.route("/connect_fitbit")
def connect_fitbit():
	return render_template("connect_fitbit.html")

@app.route("/connect_attempt")
def connect_attempt():
	url, _ = authd_client.authorize_token_url(redirect_uri=REDIRECT_URI)
	return redirect(url)

@app.route("/receive_fitbit")
def receive_fitbit():
	code = request.args.get('code')
	if code:
		authd_client.fetch_access_token(code, REDIRECT_URI)
		global FITBIT_ACCESS_TOKEN
		global FITBIT_REFRESH_TOKEN
		FITBIT_ACCESS_TOKEN = authd_client.token['access_token']
		FITBIT_REFRESH_TOKEN = authd_client.token['refresh_token']
	return redirect(url_for('fatty_stats'))


@app.route("/francis")
def fatty_stats():
	daily_data = get_daily(FITBIT_ACCESS_TOKEN, FITBIT_REFRESH_TOKEN)
	total_data = get_total(FITBIT_ACCESS_TOKEN, FITBIT_REFRESH_TOKEN)
	num_steps = []
	for item in daily_data['activities-steps']:
		num_steps.append([item['dateTime'], item['value']])
	days = list(map(lambda x: x[0], num_steps))
	steps = list(map(lambda x: int(x[1]), num_steps))
	return render_template('francis.html', days=json.dumps(days), steps=json.dumps(steps))

@app.route("/commander")
def commander_view():
	return render_template('commander.html')

def get_daily(_access_token, _refresh_token):
	client = fitbit.Fitbit(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET,
		access_token=_access_token, refresh_token=_refresh_token)

	return client.time_series("activities/steps", base_date = "today", period='7d')

def get_total(_access_token, _refresh_token):
	client = fitbit.Fitbit(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET,
		access_token=_access_token, refresh_token=_refresh_token)

	return client.activity_stats()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
