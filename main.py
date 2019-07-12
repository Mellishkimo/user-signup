from flask import Flask, redirect, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('signup.html')

@app.route("/welcome", methods=['POST'])
def validate_information():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "":
        user_error = "Please enter a username."
    elif len(username) < 3 or len(username) > 20:
        user_error = "Your username must be no fewer than 3 characters and no greater than 20 characters in length."
        username = ""
    elif " " in username:
        user_error = "Your username cannot contain spaces."
        username = ""

    if password == "":
        password_error = "Please enter a password."
    elif len(password) < 3 or len(password) > 20:
        password_error: "Your password must be no fewer than 3 characters and no greater than 20 characters in length."
    elif " " in password:
        password_error = "Your password cannot contain spaces."
    
    if verify_password == "" or verify_password != password:
        verify_error = "Please re-enter the same password."
    
  
    if email != "": 
        if email.count('@') != 1 or email.count('.') != 1:
            email_error = "You must enter a valid e-mail address."
        
    
    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template(
            'signup.html',
            username = username,
            user_error = user_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error
)
        


app.run()
