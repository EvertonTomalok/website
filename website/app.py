# coding: utf-8

from flask import Flask, url_for, render_template, redirect, request, flash
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
app.secret_key = b'@afdwap2i124Safmo13591_)(+=.,s24_0921asQWfdqe'


@app.route('/')
def redirecionar_index():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    """
    Página inicial
    """

    return render_template('index.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
