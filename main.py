from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        name = request.form['USERNAME']
        password = request.form['PASSWORD']
        return render_template('login.html', n=name, p=password)
    else:
        return "<h1>login failed</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
