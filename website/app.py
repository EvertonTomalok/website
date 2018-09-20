# coding: utf-8

from flask import Flask, url_for, render_template, redirect, request
from controllers.controllers import *


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


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        autor = request.form.get('autor', '')
        mensagem = request.form.get('mensagem', '')
        email = request.form.get('email', '')

        insert_message(autor, mensagem, email)

        return redirect('contato')

    data = []
    conteudo = find_messages()

    for cont in conteudo:
        cont['data'] = cont['data'].strftime('%d/%m/%y %H:%M:%S')
        data.append(cont)

    return render_template('contato.html', data=data)


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)

