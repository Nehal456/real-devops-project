import os
import time
from flask import Flask, jsonify
import psycopg2
from prometheus_flask_exporter import
PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(

host=os.environ.get('DB_HOST',
'localhost'),
database=os.environ.get('DB_PASSWORD',
'password')

            )
            return conn
        except psycopg2.OperationalError:
            print("Database not ready yet...")

            time.sleep(2)
            retries -= 1
    raise Exception("Could not connect to database")
@app.route('/')
def hello():
    return jsonify({"status": "success", "message",: "Hello from the real Devops Project!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.route(host='0.0.0.0', port=5000)
