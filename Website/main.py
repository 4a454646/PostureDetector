from flask import Flask, render_template, request
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/')
def hello_world():
  return render_template("status.html")

@app.route('/', methods=['POST'])
def hellow_world_post():
  first_name = request.form['fname']
  last_name = request.form['lname']
  return render_template("home.html", message = "You are a loser, " + first_name + " " + last_name)

  
app.run(host='0.0.0.0', port=8080)