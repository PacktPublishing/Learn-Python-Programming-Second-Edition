from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('main.html', name=name)


# start with:
# $ FLASK_APP=main.py flask run
