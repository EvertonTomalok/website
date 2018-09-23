# coding: utf-8

from flask import Flask, url_for, render_template, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash

from controllers.controllers import *


app = Flask(__name__)
app.secret_key = generate_password_hash('@afdwap2i124Safmo13591_)(+=.,s24_0921asQWfdqe')
DEBUG = False

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):

    def __init__(self, _id):
        self.id = _id
        self.name = "user Admin"

    def __repr__(self):
        return "%s%s" % (self.id, self.name)


@app.route('/admin', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        login = request.form.get('login', '')
        senha = request.form.get('senha', '')

        if login == "admin" and senha == "senhaforte#sqn":
            log = True
        else:
            log = False

        if log is True:
            login_user(User(1))
            return redirect(url_for('page_admin'))

        return render_template('login.html', invalido=True)

    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html')


@app.route('/pageAdmin')
@login_required
def page_admin():

    data = []
    conteudo = find_messages()

    for cont in conteudo:
        cont['data'] = cont['data'].strftime('%d/%m/%y %H:%M:%S')
        data.append(cont)

    return render_template('admin.html', data=data)


@app.route('/deletarMensagem')
def del_message():
    _id = request.args.get('_id', None)

    if _id is not None:
        delete_message_by_id(_id)

    return redirect(url_for('page_admin'))


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login.html', logar=True)


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

