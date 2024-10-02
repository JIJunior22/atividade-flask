from flask import Flask, render_template, request, redirect, url_for, session, make_response
import dao

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def hello_world():
    return render_template('cadastrarUser.html')


@app.route("/home")
def home():
    return render_template('index.html')


@app.route('/logar', methods=['POST', 'GET'])
def fazer_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        login = request.form.get('usuario')
        senha = request.form.get('password')

        if dao.verificarLogin(login, senha):
            session['userName'] = login
            print("Login realizado!")
            return redirect(url_for('home'))

        else:
            print("Erro! Login não realizado.")
            return render_template('login.html', error='Usuário ou senha incorretos.')


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
        return redirect(url_for('fazer_login'))
    else:
        print("Erro! Cadastro não realizado.")
        return render_template('cadastrarUser.html', erro="Erro no cadastro, tente novamente")


@app.route("/cadastroProduto", methods=["GET", "POST"])
def cadastrarProduto():
    if request.method == "GET":
        return render_template("produto.html")

    if request.method == "POST":
        nome = request.form["nome"]
        qtde = request.form["qtde"]
        preco = request.form["preco"]
        loginUser = session.get("userName")

        try:

            dao.inserirProduto(nome, qtde, preco, loginUser)
            print("Produto: " + nome + " cadastrado com sucesso! " + "Usuario: " + loginUser)
            return redirect(url_for("listar_produtos"))
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return render_template("produto.html", error="Erro ao cadastrar o produto. Tente novamente.")


@app.route("/cadastrarUser")
def renderizar():
    return render_template('cadastrarUser.html')


@app.route("/logout")
def logout():
    session.pop('userName', None)
    return make_response(render_template('login.html'))


@app.route('/listar-produtos', methods=['GET'])
def listar_produtos():
    try:
        produtos = dao.lista_produtos()

        #verifica se esse caraio é nulo
        if produtos is None:
            produtos = []

        return render_template('listar-produtos.html', produtos=produtos)
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return render_template('listar-produtos.html', produtos=[])



if __name__ == '__main__':
    app.run(debug=True)
