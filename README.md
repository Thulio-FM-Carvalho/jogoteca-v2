# Jogoteca

* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Aplicação](#aplicação)
* [Ferramentas utilizadas](#ferramentas-utilizadas)
* [Frameworks e tecnologias utilizadas](#frameworks-e-tecnologias-utilizadas)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)

# Descrição do projeto
Este projeto é 2° parte do 2° curso de Flask da Alura. Este projeto é uma Aplicação web que permite cadastrar, listar, editar, remover jogos e fazer login e logout de um usuário. 
Com um sistema de autorização implementado, só será permitido cadastrar, editar e remover um jogo se o usuário estiver logado. A cada jogo cadastrado será salvo no banco de dados. As listagens de jogos, edição e remoção que são realizadas são execuções a partir de queries executadas em SQL.

# Funcionalidades
 - ✔️ `Funcionalidade 1`: Realizar login e logout com lógica de autorização
 - ✔️ `Funcionalidade 2`: Adicionar um jogo contendo o nome, categoria, console e opção de fazer upload da imagem do jogo
 - ✔️ `Funcionalidade 3`: Listar todos os jogos
 - ✔️ `Funcionalidade 4`: Editar um jogo
 - ✔️ `Funcionalidade 5`: Remover um jogo
 
# Aplicação

![GIF 20-12-2022 21-40-27](https://user-images.githubusercontent.com/48070981/208794686-bd464ce0-94d6-4af6-b05e-370a96caeed2.gif)

# Ferramentas utilizadas
- `PyCharm`
- `MySQL Workbench`

# Frameworks e tecnologias utilizadas
- `Flask`
- `SQLAlchemy`
- `Paradigma de Orientação a objetos`
- `Padrão MVC(Model, View Controller)`
- `Python`
- `HTML`
- `SQL`

# Abrir e rodar o projeto
Após baixar o projeto, você pode abrir com o PyCharm. Para isso, na tela de launcher clique em:

- Open;
- Procure o local onde o projeto está e o selecione (Caso o projeto seja baixado via zip, é necessário extraí-lo antes de procurá-lo);
- Por fim clique em OK;

Se necessário, configurar o Python interpreter e fazer a instalação das bibliotecas incluídas no arquivo ```requirements.txt```. Abra o arquivo ```prepara_banco.py```, coloque o usuario e a senha da conexão do banco de dados, salve o arquivo e o execute. Após a execução, agora foi criado um banco de dados para armazenar os jogos que serão cadastrados e obter os dados de login de usuário. Feito isso, execute a o arquivo ```jogoteca.py``` e será mostrado no console da aplicação um link, e ao clicar no link, será aberto um navegador de internet com a aplicação já em execução. 🏆

# Autores

| [<img src="https://avatars.githubusercontent.com/u/48070981?s=400&v=4" width=115><br><sub>Thulio Carvalho</sub>](https://github.com/Thulio-FM-Carvalho) |  
| :---: |
