import psycopg2

import dao


def conectar():
    con = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='root'
    )
    return con


def verificarLogin(nome, senha):
    conexao = conect()
    cur = conexao.cursor()
    cur.execute(f"SELECT count(*) from usuario where loginuser ='{nome}' and senha='{senha}'")
    recset = cur.fetchall()
    conexao.close()

    if recset[0][0] == 1:
        return True
    else:
        return False


def inserirProduto(nome, qtde, preco, user):
    conexao = conect()
    cur = conexao.cursor()

    cur.execute("SELECT count(*) FROM produtos WHERE loginuser = %s", (user,))
    recset = cur.fetchone()

    QtdeProduto = recset[0]

    if user == "normal" and QtdeProduto >= 3:
        print("Limite de produtos atingido para usuários normais")
        conexao.close()
        return False
    else:
        cur.execute("INSERT INTO produtos (nome, qtde, preco, loginuser) VALUES (%s, %s, %s, %s)",
                    (nome, qtde, preco, user))
        conexao.commit()
        conexao.close()
        return True


def inserirUsuario(loginuser, senha, tipouser):
    conexao = conect()
    cur = conexao.cursor()
    try:
        cur.execute(
            f"INSERT INTO usuario VALUES ('{loginuser}', '{senha}', '{tipouser}')"
        )
        conexao.commit()

        conexao.close()
        return True

    except Exception as e:
        print(f"Erro ao inserir usuario: {e}")
        conexao.rollback()

        return False


def verificarLoginExistente(login):
    conexao = conect()
    cur = conexao.cursor()

    cur.execute("SELECT COUNT(*) FROM usuario WHERE loginUser = %s", (login,))
    result = cur.fetchone()

    cur.close()
    conexao.close()

    return result[0] > 0


def verificarTipoUsuario(tipo_usuario):
    conexao = conect()
    cur = conexao.cursor()

    cur.execute(f"select tipouser from usuario where tipouser=%s", (tipo_usuario))
    result = cur.fetchone()

    cur.close()
    conexao.close()

    if result:
        return [0]
    else:
        return None


def userTypeValidation(tipo_user):
    tipo = verificarTipoUsuario(tipo_user)

    if tipo == 'normal':
        conexao = conect()
        cur = conexao.cursor()

        cur.execute("SELECT COUNT(*) FROM produtos WHERE loginuser = %s", (tipo_user))
        total_prod = cur.fetchone()[0]
        cur.close()
        conexao.close()

        if total_prod >= 3:
            return False, 'Limite de cadastro atingido'
        else:
            return True
    if tipo == 'super':
        conexao = conect()
        cur = conexao.cursor()

        cur.execute("SELECT COUNT(*) FROM produtos WHERE loginuser = %s", (tipo_user))
        total_prod = cur.fetchone()[0]
        cur.close()
        conexao.close()

        if total_prod >= 3:
            return False, 'Limite de cadastro atingido'
        else:
            return True


def conect():
    return conectar()


def lista_produtos():
    conexao = conect()
    cur = conexao.cursor()

    try:
        cur.execute("SELECT nome, qtde, preco FROM produtos")
        produtos = cur.fetchall()

        # Se não houver produtos, retorna uma lista vazia
        if not produtos:
            return []

        return produtos
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return []
    finally:
        conexao.close()

