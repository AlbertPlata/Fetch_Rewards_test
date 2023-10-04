import psycopg2
import json
#Connection Parameters
db_host = "0.0.0.0"
db_port = 5432
db_name = "fetch_challenges"
db_user = "postgres"
db_password = "postgres"

# Connection
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

cur = conn.cursor()

# Create staging table
create_table_query = '''
CREATE TABLE IF NOT EXISTS user_logins (
    user_id varchar(128),
    device_type varchar(32),
    masked_ip varchar(256),
    masked_device_id varchar(256),
    locale varchar(32),
    app_version integer,
    create_date date
);
'''
cur.execute(create_table_query)
conn.commit()

# Load the masked JSON data into the user_logins table
with open("masked_messages.json", "r") as json_file:
    masked_messages = json.load(json_file)
    for message in masked_messages:
        #Ussually I use f"" string to concatenate the data but on this way prevent injections
        insert_query = '''
        INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        '''
        cur.execute(insert_query, (
            message["user_id"],
            message["device_type"],
            message["masked_ip"],
            message["masked_device_id"],
            message["locale"],
            message["app_version"],
            message["create_date"]
        ))


conn.commit()
conn.close()
