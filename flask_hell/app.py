from flask import Flask
app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/integer/<int:value>")
def int_type(value):
	value += 2
	print (value)
	return "incorrect!!!!!"

@app.route("/float/<float:value>")
def float_type(value):
	print (value + 2)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print (value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower()=="one":
		return "onehell, {}".format(name), 200
	else:
		return "not found", 404




if __name__ == "__main__":
	app.run()