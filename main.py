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

        length_username = len(user_name)
        length_password = len(pass_word)

        if not user_name:
            error_message = "Incomplete form"

        if length_username < 3 or length_username > 20:
            error_message = "Invalid username"

        if not pass_word:
            error_message = "Incomplete form"

        if length_password < 3 or length_password > 20:
            error_message = "Invalid password"    

        if not verifypass:
            error_message = "Incomplete form"     

        if pass_word != verifypass:
            error_message = "Passwords do not match"           

    return render_template("sign_in.html", error=error_message)

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")
    
app.run()
