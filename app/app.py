from flask import Flask, request
from flask_restx import Api, Resource, fields
import psycopg2

app = Flask(__name__)
api = Api(app, version='1.0', title='API de Operações',
          description='API para cálculos matemáticos e gestão de clientes')

ns_math = api.namespace('matematica', description='Operações matemáticas')
ns_db = api.namespace('clientes', description='Gestão de clientes')

math_model = api.model('EntradaMatematica', {
    'num1': fields.Float(required=True),
    'num2': fields.Float(required=True)
})

@ns_math.route('/soma')
class Soma(Resource):
    @ns_math.expect(math_model)
    def post(self):
        """Soma dois números"""
        dados = request.get_json()
        return {"resultado": dados['num1'] + dados['num2']}, 200

@ns_math.route('/multiplicacao')
class Multiplicacao(Resource):
    @ns_math.expect(math_model)
    def post(self):
        """Multiplica dois números"""
        dados = request.get_json()
        return {"resultado": dados['num1'] * dados['num2']}, 200

@ns_db.route('/')
class Clientes(Resource):
    def get(self):
        """Lista todos os clientes"""
        conn = psycopg2.connect(
            host='db',
            database='meu_db',
            user='postgres',
            password='root',
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes")
        result = [{'id': row[0], 'nome': row[1]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return result, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
