from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Configuração do banco
db_config = {
    'dbname': 'escola',
    'user': 'admin',
    'password': 'admin',
    'host': 'db',
    'port': 5432
}

# Conexão com o banco de dados
def connect_db():
    return psycopg2.connect(**db_config)

# Listar alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return jsonify(alunos)

# Cadastrar aluno
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (data['aluno_id'], data['nome'], data.get('endereco'), data.get('cidade'), data.get('estado'), data.get('cep'), data.get('pais'), data.get('telefone')))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201

# Alterar aluno
@app.route('/alunos/<aluno_id>', methods=['PUT'])
def alterar_aluno(aluno_id):
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE alunos SET nome=%s, endereco=%s, cidade=%s, estado=%s, cep=%s, pais=%s, telefone=%s
        WHERE aluno_id=%s
    """, (data['nome'], data.get('endereco'), data.get('cidade'), data.get('estado'), data.get('cep'), data.get('pais'), data.get('telefone'), aluno_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Aluno atualizado com sucesso!'})

# Excluir aluno
@app.route('/alunos/<aluno_id>', methods=['DELETE'])
def excluir_aluno(aluno_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE aluno_id=%s", (aluno_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Aluno excluído com sucesso!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
