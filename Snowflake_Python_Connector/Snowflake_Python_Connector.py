import snowflake.connector

# Connectio string
conn = snowflake.connector.connect(
                user='snuser',
                password='password@123',
                account='xyz12345.us-east-2',
                #warehouse='COMPUTE_WH',
                database='DEMO_DB',
                schema='public'
                )

# Create cursor
cur = conn.cursor()

# Execute SQL statement
cur.execute("select current_date;")

