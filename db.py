import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS readings (
                time TIMESTAMP PRIMARY KEY,
                pm10 REAL,
                pm2_5 REAL
            )
        """)
    conn.commit()

def save(conn, df):
    # pandas NaN must become None so Postgres stores NULL
    df = df.astype(object).where(df.notna(), None)
    rows = list(df[["time", "pm10", "pm2_5"]].itertuples(index=False, name=None))
    
    with conn.cursor() as cur:
        execute_values(cur, """
            INSERT INTO readings (time, pm10, pm2_5) VALUES %s
            ON CONFLICT (time) DO NOTHING
        """, rows)
        inserted = cur.rowcount
        
    conn.commit()
    return inserted