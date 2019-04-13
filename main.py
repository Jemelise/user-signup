from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET", "POST"])
def user_signup():

    error_message = ""
    if request.method == "POST":
        user_name = request.form['username']
        pass_word = request.form['password']
        verifypass = request.form['verify']
        email = request.form['email']

        if not user_name:
            error_message = "Incomplete form"

        if not pass_word:
            error_message = "Incomplete form"

        if not verifypass:
            error_message = "Incomplete form"            

    return render_template("sign_in.html", error=error_message)

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")



app.run()
