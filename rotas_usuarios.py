from helpers import FormularioUsuario
from models import Usuarios
from app import app
from flask import render_template, request, redirect, session, flash, url_for
from flask_bcrypt import check_password_hash

# Rota de login que retorna o formulário para digitar as credenciais e fazer o login


@app.route('/login')
def login():
    # capturando a informação da queryString
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = "/"
    # enviando as informações da proxima pagina pro html
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)


# session é um atributo flask que guarda as informações do usuário nos coockies do navegador
# rota responsável por realizar a autenticação do login
# Se o usuário que a pessoa digitou estiver na lista de usuarios cadastrada no sistema,
# verifica se a senha que a pessoa digitou é a mesma senha do usuário cadastrado no sistema,
# cria uma sessão, imprime na tela o sucesso da operação e redireciona para proxima pagina.
@app.route('/autenticar', methods=['POST'], )
def autenticar():

    form = FormularioUsuario(request.form)

    #pegando o usuario no banco de dados cujo o nickname é o mesmo digitado no formulário
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    #validando se a senha fornecida é a mesma senha do banco de dados
    #senha = check_password_hash(usuario.senha, form.senha.data)
    senha = usuario.senha == form.senha.data

    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        # passando dentro do url_for a função que instancia a rota login, que é o /login
        return redirect(url_for('login'))

# Rota responsável por finalizar a sessão do usuário
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    # passando dentro do url_for a função que instancia a rota index, que é o barra /
    return redirect(url_for('index'))
