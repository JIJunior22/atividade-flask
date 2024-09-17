from flask import *

import dao

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def hello_world():  # put application's code here
    return render_template('cadastrarUser.html')


@app.route('/logar', methods=['POST', 'GET'])
def fazer_login():
    if 'GET' == request.method:
        return render_template('login.html')
    elif request.method == 'POST':
        login = request.form.get('usuario')
        senha = request.form.get('password')

        if dao.verificarLogin(login, senha):
            session['userName'] = login
            print("Login realizado!")
            return render_template('produto.html', user=login)

        else:

            print("Erro! Login não realizado.")
            return render_template('login.html')


@app.route("/cadastrar/usuario", methods=['POST'])
def cadastrar_usuario():
    login = request.form.get('usuario')
    senha = request.form.get('password')
    tipouser = request.form.get('usertype')

    if dao.verificarLoginExistente(login):
        print("Erro! Login já existe.")
        return render_template('cadastrarUser.html', erro="Usuário já existe")

    if dao.inserirUsuario(login, senha, tipouser):
        print("Cadastro realizado com sucesso!")
        return render_template('index.html', sucesso="Cadastro realizado com sucesso!")
    else:
        print("Erro! Cadastro não realizado.")
        return render_template('cadastrarUser.html', erro="Erro no cadastro, tente novamente")


@app.route('/cadastrar/produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'GET':
        return render_template('produto.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        preco = request.form.get('preco')

        dao.inserirUsuario(nome, quantidade, preco)

        return f'Produto cadastrado com sucesso! Nome: {nome}, Quantidade: {quantidade}, Preço: {preco}'


@app.route("/cadastrar")
def renderizar():
    return render_template('cadastrarUser.html')


if __name__ == '__main__':
    app.run(debug=True)
