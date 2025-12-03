import os
from flask import Flask, jsonify
import psycopg2 

app = Flask(__name__)

# Variables externes
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('POSTGRES_DB', 'generic_app_db')
DB_USER = os.getenv('DB_USER', 'app_user_db')
DB_PASS = os.getenv('DB_PASSWORD', 'password')
API_PORT = int(os.getenv('API_PORT', 8080))

def get_db_connection():
    # Connexion BDD
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/status') 
def status():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "OK", "database_status": "Connected"}), 200
    except Exception as e:
        return jsonify({"status": "Error", "database_status": str(e)}), 500

@app.route('/items') 
def get_items():
    items = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM items;")
        items = [{'id': row[0], 'name': row[1], 'description': row[2]} for row in cur.fetchall()]
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": "Failed to retrieve items", "details": str(e)}), 500
    return jsonify(items), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_PORT)