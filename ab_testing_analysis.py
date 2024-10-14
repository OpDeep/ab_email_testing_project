import psycopg2
import pandas as pd
from scipy import stats

# Database connection
def get_data():
    conn = psycopg2.connect(
        host="localhost",
        database="ab_testing",
        user="your_username",
        password="your_password"
    )
    query = "SELECT variant, COUNT(open) AS opens, COUNT(click) AS clicks FROM email_campaigns GROUP BY variant"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# A/B Testing statistical significance using Chi-Square test
def ab_test_analysis(df):
    open_A = df[df['variant'] == 'A']['opens'].values[0]
    open_B = df[df['variant'] == 'B']['opens'].values[0]
    total_A = df[df['variant'] == 'A']['opens'].sum()
    total_B = df[df['variant'] == 'B']['opens'].sum()

    data = [[open_A, total_A - open_A], [open_B, total_B - open_B]]
    chi2, p_value = stats.chi2_contingency(data)[:2]

    print(f"Chi-Square Test Result: p-value={p_value}")
    if p_value < 0.05:
        print("Significant difference between A and B")
    else:
        print("No significant difference")

if __name__ == '__main__':
    data = get_data()
    print(data)
    ab_test_analysis(data)
