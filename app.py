from flask import Flask, render_template, request, redirect, session
import psutil

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database to store registered users
registered_users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in registered_users and registered_users[username] == password:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password.')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) < 6 or len(password) < 6:
            return render_template('signup.html', error='Username and password must be at least six characters long.')
        registered_users[username] = password
        session['username'] = username
        return redirect('/')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/portfolio')
def portfolio():
    if 'username' in session:
        return render_template('portfolio.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/monitoring')
def monitoring():
    if 'username' in session:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        return render_template('monitoring.html', username=session['username'], cpu_usage=cpu_usage, memory_usage=memory_usage)
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)



