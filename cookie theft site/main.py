from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
from werkzeug.security import check_password_hash, generate_password_hash
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'super_secret' 

# --- Session Security Configuration (VULNERABLE FOR DEMO) ---
# For demoing cookie theft via XSS, we intentionally set HttpOnly to False.
app.config['SESSION_COOKIE_HTTPONLY'] = False 
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10) # Session expires after 10 minutes of inactivity
# --- End Session Security Configuration ---

# Ensure users.json exists, create if not
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump({}, f)

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('users.json', 'r') as file:
            users = json.load(file)

        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            session.permanent = True # 10 min lifetime
            flash(f'Welcome, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        with open('users.json', 'r') as file:
            users = json.load(file)

        if username in users:
            flash('Username already exists. Please choose a different one.', 'error')
            return render_template('signup.html')

        if password == confirm_password:
            hashed_password = generate_password_hash(password)
            users[username] = {'password': hashed_password}

            with open('users.json', 'w') as file:
                json.dump(users, file, indent=4)

            flash(f'Account created successfully for {username}! Please login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match.', 'error')

    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        content_display = request.args.get('q', 'Dashboard')
        if(content_display == 'Dashboard'):
            return render_template('dashboard.html', username=session['username'])
        
        return render_template('contents.html', username=session['username'], content_display=content_display)
    else:
        flash('You need to log in first.', 'info')
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)