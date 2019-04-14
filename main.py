from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET", "POST"])
def user_signup():
    user_name = ""
    incomplete_verify_error_message = ""
    incomplete_un_error_message = ""
    incomplete_pass_error_message = ""
    username_error_message = ""
    password_error_message = ""
    verify_error_message = ""
    email_error_message = ""
    email = ""

    if request.method == "POST":

        user_name = request.form['username']
        pass_word = request.form['password']
        verifypass = request.form['verify']
        email = request.form['email']

        length_username = len(user_name)
        length_password = len(pass_word)
        length_email = len(email)

        if not user_name:
            incomplete_un_error_message = "*Incomplete form, enter username"

        if length_username < 3 or length_username > 20:
            username_error_message = "Invalid username"

        if not pass_word:
            incomplete_pass_error_message = "*Incomplete form, enter password"

        if length_password < 3 or length_password > 20:
            password_error_message = "Invalid password"    

        if not verifypass:
            incomplete_verify_error_message = "*Incomplete form, verify password"     

        if pass_word != verifypass:
            verify_error_message = "Passwords do not match"    

        if email:
            if length_email < 3 or length_email > 20:
                email_error_message = "Invalid email"  

            if "@" not in email:
                email_error_message = "Invalid email"

            if "." not in email:
                email_error_message = "Invalid email"

            if " " in email:
                email_error_message = "Invalid email"                           

        if not (incomplete_un_error_message, incomplete_verify_error_message,
            incomplete_pass_error_message):
            return render_template("welcome.html", user_name=user_name)       

    return render_template("sign_in.html", incomplete_verify_error_message=incomplete_verify_error_message, 
    incomplete_un_error_message=incomplete_un_error_message, 
    incomplete_pass_error_message=incomplete_pass_error_message,
    username_error_message=username_error_message, password_error_message=password_error_message, 
    verify_error_message=verify_error_message, email_error_message=email_error_message, 
    user_name=user_name, email=email)

@app.route("/welcome", methods=["POST"])
def welcome():
    user_name = request.form['username']
    return render_template("welcome.html", user_name=user_name)

app.run()
