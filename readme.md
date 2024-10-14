
# A/B Testing for Email Campaigns

## Project Description

This project demonstrates how A/B testing is used to optimize email campaigns by experimenting with different variations in subject lines, email content, and send times. The goal is to analyze the results and implement the best practices for future email campaigns, ultimately leading to improved open rates and click-through rates.

Key tools used include Python for analyzing the results, PostgreSQL for storing data, SQL for queries, and Excel for presenting findings.

## Features

- **A/B Testing**: Tests variations of subject lines, email content, and send times.
- **Data Storage**: PostgreSQL is used to store the test results.
- **Analysis**: SQL queries to fetch and analyze the data.
- **Visualization**: Results and insights are presented using Excel.

## Technologies Used

- **Python**: Used for performing analysis and scripting.
- **PostgreSQL**: For database management and storing test data.
- **SQL**: Used for querying test results.
- **Excel**: For compiling and presenting data insights.

## Project Setup

### Prerequisites

- **Python 3.x**: [Install Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Install PostgreSQL](https://www.postgresql.org/download/)
- **Excel**: For result presentation.

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/OpDeep/ab_email_testing_project.git
   cd ab-testing-email-campaigns
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup PostgreSQL:
   - Install PostgreSQL and create a database named `ab_testing`.
   - Run the provided SQL file to set up the database schema:
     ```bash
     psql -U <your-username> -d ab_testing -f db_setup.sql
     ```

4. Run the Python analysis script:
   ```bash
   python analyze_ab_test.py
   ```

## Database Schema

The `emails` table stores the details of each test email:

| Column       | Type     | Description                      |
|--------------|----------|----------------------------------|
| `id`         | SERIAL   | Unique email ID                  |
| `subject`    | TEXT     | Email subject line               |
| `content`    | TEXT     | Content of the email             |
| `send_time`  | TIMESTAMP| Time the email was sent          |
| `open`       | BOOLEAN  | Whether the email was opened     |
| `click`      | BOOLEAN  | Whether a link in the email was clicked |

## Results & Insights

- **Higher Open Rates**: Subject lines that were personalized with the recipient's name had a higher open rate.
- **Click-Through Rates**: Emails sent at 10 AM on weekdays had the highest click-through rate.
- **Content Analysis**: Shorter, more concise content outperformed longer, detailed emails.


