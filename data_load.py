import psycopg2
import csv

def load_data():
    conn = psycopg2.connect(
        host="localhost",
        database="ab_testing",
        user="your_username",
        password="your_password"
    )
    cur = conn.cursor()
    
    with open('email_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO email_campaigns (email_id, variant, send_time, open, click) VALUES (%s, %s, %s, %s, %s)",
                row
            )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    load_data()
