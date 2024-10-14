
CREATE TABLE email_campaigns (
    campaign_id SERIAL PRIMARY KEY,
    email_id VARCHAR(255),
    variant VARCHAR(10),       -- A or B
    send_time TIMESTAMP,
    open BOOLEAN,
    click BOOLEAN
);
