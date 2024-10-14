import pandas as pd
import psycopg2

def export_to_excel():
    conn = psycopg2.connect(
        host="localhost",
        database="ab_testing",
        user="your_username",
        password="your_password"
    )
    
    query = "SELECT * FROM email_campaigns"
    df = pd.read_sql(query, conn)
    
    # Write to Excel
    with pd.ExcelWriter('ab_test_report.xlsx') as writer:
        df.to_excel(writer, sheet_name='Campaign Data', index=False)
    
    conn.close()
    print("Report generated: ab_test_report.xlsx")

if __name__ == '__main__':
    export_to_excel()
