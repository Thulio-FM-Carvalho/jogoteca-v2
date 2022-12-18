from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from models import Jogos
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo
import time


# rota padrão responsável por retornar a lista de jogos já cadastrados
@app.route('/', methods=['GET'])
def index():
    # buscando a lista de jogos no BD
    lista_jogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


# rota responsável por chamar o formulário para cadastrar novos jogos
# se não tiver nenhum usuario logado na sessão, redireciona para a pagina de login para ser efetuar o login,
# e assim que o login for realizado, redireciona para a pagina com o formulario para cadastrar o novo jogo
@app.route('/novo', methods=['GET'])
def novo():
    # se não tiver nenhum usuário logado na sessão, ou se não tiver um usuario logado, redireciona para a rota login
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # passando dentro do url_for a função que instancia a rota login, redirecionando para a pagina de /novo
        return redirect(url_for('login', proxima=url_for('novo')))

    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form)


# rota responsável por puxar as informações do novo.html e cadastrar um novo jogo
# capturando o nome, categoria e console da pessoa que digitou no formulário, adicionando na lista de jogos
# e redireciona para pagina index para listar os jogos.
@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioJogo(request.form)

    # validando se o formulario é foi preenchid corretamente ou não, TRUE OR FALSE
    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

    # pegando o jogo no banco de dados cujo o nome é o mesmo digitado no formulário
    jogo = Jogos.query.filter_by(nome=nome).first()

    # se jogo já existe no banco de dados redireciona para a pagina de index
    if jogo:
        flash('Jogo já existente')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()  # adicionando o jogo no banco de dados

    # pegando a imagem
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']

    timestamp = time.time()

    # salvando a imagem com o nome do id do novo jogo no servidor
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


# rota responsável por chamar o formulário para editar o jogo específico
# recebendo como parametro o ID do jogo que o usuario clicou no botão editar
@app.route('/editar/<int:id>')
def editar(id):
    # se não tiver nenhum usuário logado na sessão, ou se não tiver um usuario logado, redireciona para a rota login
    # e assim que é efetuado o login redireciona para proxima rota de editar passando o ID do jogo
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))

    # pegando o jogo cujo o id do jogo é o mesmo id no banco de dados
    jogo = Jogos.query.filter_by(id=id).first()

    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    capa_jogo = recupera_imagem(id)

    # renderiza o editar.html, passando o titulo e o jogo capturado do banco de dados
    return render_template('editar.html', titulo='Editando Jogo', id=id, capa_jogo=capa_jogo, form=form)


@app.route('/atualizar', methods=['POST'])
def atualizar():
    form = FormularioJogo(request.form)

    # se o formulario for validado
    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.add(jogo)
        db.session.commit()

        # pegando a imagem
        arquivo = request.files['arquivo']

        upload_path = app.config['UPLOAD_PATH']

        timestamp = time.time()

        deleta_arquivo(jogo.id)  # deletando a imagem anterior

        # salvando a imagem com o nome do id do novo jogo no servidor
        arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')

        flash('Jogo atualizado com sucesso!')
    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    # se não tiver nenhum usuário logado na sessão, ou se não tiver um usuario logado, redireciona para a rota login
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
