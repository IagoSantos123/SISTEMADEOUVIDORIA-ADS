import mysql.connector
from Backend.config import DB_CONFIG

def conectar():
    """Conecta ao banco de dados."""
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

def listar_manifestacoes():
    """Lista todas as manifestações registradas."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM manifestacoes")
        manifestacoes = cursor.fetchall()
        for m in manifestacoes:
            print(m)
        cursor.close()
        conexao.close()

def inserir_manifestacao(tipo, descricao):
    """Insere uma nova manifestação."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)"
        cursor.execute(sql, (tipo, descricao))
        conexao.commit()
        print("Manifestação registrada com sucesso!")
        cursor.close()
        conexao.close()

def alterar_manifestacao(id, novo_tipo, nova_descricao):
    """Altera uma manifestação existente."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE manifestacoes SET tipo = %s, descricao = %s WHERE id = %s"
        cursor.execute(sql, (novo_tipo, nova_descricao, id))
        conexao.commit()
        print("Manifestação alterada com sucesso!")
        cursor.close()
        conexao.close()

def excluir_manifestacao(id):
    """Exclui uma manifestação."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM manifestacoes WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        print("Manifestação excluída com sucesso!")
        cursor.close()
        conexao.close()
