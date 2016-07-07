from flask import Flask, render_template
app =  Flask(__name__)

@app.route('/')			
def landing():
	return render_template('index.html')

@app.route('/ninjas')
def success():
	return render_template('ninjas.html')

@app.route('/dojos/new')
def success():
	return render_template('dojos.html')

app.run(debug=True)