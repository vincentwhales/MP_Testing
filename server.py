from flask import Flask, render_template

app = Flask(__name__)


@app.route('/1')
def one():
    return render_template('one.html')


@app.route('/2')
def two():
    return render_template('two.html')
