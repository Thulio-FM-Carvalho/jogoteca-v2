import os

SECRET_KEY = 'alura' # adicionando camada de criptografia no site

SQLALCHEMY_DATABASE_URI = "postgresql://jogotecav2_postgres_user:Xl8cHnFJLYxRB1GUFKOI9jkZ0twVLCLS@dpg-cf26p5mn6mpkr6dh3hu0-a.oregon-postgres.render.com/jogotecav2_postgres"
#fazendo a conexão com o banco de dados
# SQLALCHEMY_DATABASE_URI = \
    #'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        #SGBD = 'mysql+mysqlconnector',
        #usuario = 'root',
        #senha = 'root',
        #servidor = 'localhost',
        #database = 'jogoteca'
    #)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'