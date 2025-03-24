from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

@app.route('/manifestacoes', methods=['GET'])
def listar_manifestacoes():
    cursor.execute("SELECT * FROM manifestacoes")
    manifestacoes = cursor.fetchall()
    return jsonify(manifestacoes)

@app.route('/manifestacoes', methods=['POST'])
def criar_manifestacao():
    data = request.json
    cursor.execute("INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)", 
                   (data['tipo'], data['descricao']))
    conn.commit()
    return jsonify({'message': 'Manifestação criada com sucesso!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
