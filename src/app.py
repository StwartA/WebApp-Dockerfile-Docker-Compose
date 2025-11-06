from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = mysql.connector.connect(
            host="mysql_db",
            user="root",
            password="123456",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hola desde MySQL!'")
        result = cursor.fetchone()
        return f"Hola Mundo! Conexión exitosa → {result[0]}"
    except Exception as e:
        return f"Error conectando a MySQL: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
