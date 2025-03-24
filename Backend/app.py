from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM manifestacoes")
        manifestacoes = cursor.fetchall()
        return jsonify(manifestacoes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/manifestacoes', methods=['POST'])
def criar_manifestacao():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)", 
                       (data['tipo'], data['descricao']))
        conn.commit()
        return jsonify({'message': 'Manifestação criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    
    app.run(debug=True)  
