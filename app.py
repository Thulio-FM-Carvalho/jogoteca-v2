from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__) # name faz referencia ao proprio arquivo e garante que vai rodar a aplicação
app.config.from_pyfile('config.py') #puxando as configurações do arquivo config

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
cors = CORS(app)

#executando as rotas
from rotas_game import *
from rotas_usuarios import *

if __name__ == '__main__':
    app.run() # faz rodar a aplicação