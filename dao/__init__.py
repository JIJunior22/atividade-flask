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


def inserirProduto(nome, login, qtde, preco):
    conexao = conect()
    cur = conexao.cursor()

    try:

        if userTypeValidation(login):
            cur.execute(
                "INSERT INTO produtos (nome, loginUser, qtde, preco) VALUES (%s, %s, %s, %s)",
                (nome, login, qtde, preco)
            )
            conexao.commit()
            print("Produto inserido com sucesso!")
        else:
            print("Limite de cadastro de produtos atingido para este usuário.")

    except Exception as e:
        print(f"Erro ao inserir produto: {e}")
        conexao.rollback()

    finally:
        cur.close()
        conexao.close()


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

        cur.execute("SELECT COUNT(*) FROM produtos WHERE usuario_id = %s", (tipo_user))
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

        cur.execute("SELECT COUNT(*) FROM produtos WHERE usuario_id = %s", (tipo_user))
        total_prod = cur.fetchone()[0]
        cur.close()
        conexao.close()

        if total_prod >= 3:
            return False, 'Limite de cadastro atingido'
        else:
            return True


def conect():
    return conectar()
