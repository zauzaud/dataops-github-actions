from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/clientes', methods=['GET'])
def get_clientes():
    connection = psycopg2.connect(
        host='db',
        database='meu_db',
        user='postgres',
        password='root',
        port=5432
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    
    clientes = []
    for cliente in cursor.fetchall():
        clientes.append({'id': cliente[0], 'nome': cliente[1]})
    
    cursor.close()
    connection.close()
    
    return jsonify(clientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
