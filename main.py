from flask import Flask
from flask import render_template
from flask import request
import twitter_api

app = Flask("MyApp")


@app.route("/")
def hello():
    return render_template("hello.html")


@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())


@app.route("/bye/<name>")
def bye_someone(name):
    return render_template("bye.html",
                           name=name.title())  # templates must rest in their own folder called 'templates' and MAKE SURE YOUR FUNCTION HAVE THE RIGHT NAMES!!!


@app.route("/signup", methods=['POST'])
def sign_up():
    tweets=twitter_api.gettweets('glitter beards')
    form_data = request.form
    # print form_data['name']
    # print form_data['email']
    # return "All OK"
    render_template("project.html")


app.run(debug=True)  # debugger - prevents server clash and manial refresh
