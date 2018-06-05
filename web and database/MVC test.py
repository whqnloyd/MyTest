from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username is not None and password == 'password':
        return render_template('signin-ok.html', username=username)
    else:
        return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(debug=True)

#公开可用
#    app.debug = True
#    app.run(host='0.0.0.0')