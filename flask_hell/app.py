from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/yoyoyo")

def hell():
	return "hell yo"

if __name__ == "__main__":
	app.run()