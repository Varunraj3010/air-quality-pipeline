from db import get_connection

QUERIES = open("queries.sql").read().split(";")

def main():
    conn = get_connection()
    with conn.cursor() as cur:
        for q in QUERIES:
            q = q.strip()
            if not q:
                continue
            print("\n" + q.splitlines()[0])  # prints the comment line
            cur.execute(q)
            for row in cur.fetchall():
                print(row)
    conn.close()

if __name__ == "__main__":
    main()