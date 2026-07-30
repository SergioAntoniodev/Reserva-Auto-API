import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="uber_maintenance",
        user="postgres",
        password="14454870"
    )

    print("Conectado!")
    conn.close()

except Exception as e:
    print(type(e).__name__)
    print(repr(e))