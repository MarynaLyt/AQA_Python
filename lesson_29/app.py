from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "mydatabase"),
        user=os.getenv("POSTGRES_USER", "marynalytvynenko"),
        password=os.getenv("POSTGRES_PASSWORD", "")
    )


@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


@app.route('/test-connection')
def test_connection():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        conn.close()
        return jsonify({
            "status": "success",
            "user": "marynalytvynenko",
            "database": "mydatabase",
            "postgres_version": version
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "users": users, "count": len(users)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e), "users": [], "count": 0})


@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
                       (data['name'], data['email']))
        user_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "user_id": user_id})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s",
                       (data['name'], data['email'], user_id))
        rows = cursor.rowcount
        conn.commit()
        conn.close()
        if rows > 0:
            return jsonify({"status": "success", "message": "User updated"})
        else:
            return jsonify({"status": "error", "message": "User not found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        rows = cursor.rowcount
        conn.commit()
        conn.close()
        if rows > 0:
            return jsonify({"status": "success", "message": "User deleted"})
        else:
            return jsonify({"status": "error", "message": "User not found"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)