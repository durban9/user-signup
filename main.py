from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/user-signup')
def user_signup_form():
    return render_template('signup-form.html')


@app.route('/user-signup', methods =['POST'])    
def validate_input():
    username = request.form['Username']
    username_error=''
    password = request.form['Password']
    password_error=''
    verification = request.form['Verification']
    verification_error=''
    email = request.form['Email']
    email_error = ''
    
    
    if (username == ''):
            username_error = 'The username must not be left blank.' 
            username=''
            return render_template('signup-form.html', username=username, username_error=username_error)
    
    else: 
        if len(username) < 3 or len(username) > 20:
            username_error = 'The username must be greater than three characters or less than twenty characters.'
            username=''
            return render_template('signup-form.html', username=username, username_error=username_error)
                
    if (password == ''):
            password_error = 'The password username must not be left blank.' 
            password=''
            return render_template('signup-form.html', username=username, password=password, 
                                    password_error=password_error)
    
    else: 
        if len(password) < 3 or len(password) > 20:
            password_error = 'The username must be greater than three characters or less than twenty characters.'
            password=''
            return render_template('signup-form.html', username=username, password=password, 
                                    password_error=password_error)

    if (verification != password):
        verification_error = 'The password verification does not match the original password.'
        verification = ''
        password = ''
        return render_template('signup-form.html', username=username, password=password, verification=verification, 
                                verification_error=verification_error, email=email)

    if email == '':
        return render_template('Welcome.html', username=username)

    elif len(email) < 3 or len(email) > 20:
            email_error = 'The email must be greater than three characters or less than twenty characters.'
            password=''
            verification = ''
            return render_template('signup-form.html', username=username, verification=verification,
                                    password=password, email_error=email_error)
    
    else:
        if ('@' not in email):
            email_error ='The email must contain an '+ '@' + 'symbol.'
            password = ''
            verification = ''
            return render_template('signup-form.html', username=username, password=password, 
                                    verification=verification, email_error=email_error)                                                                
                                
        
    if not username_error and not password_error and not verification_error and not email_error:    
        return render_template('Welcome.html', username=username)


    
    

app.run()