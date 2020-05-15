from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form_input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    with open("data.txt", "a") as myfile:
    	myfile.write (text + "\n")
    return redirect(url_for('my_form'))
