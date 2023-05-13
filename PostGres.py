import psycopg2
from Backupbutton import Backupbutton
from Create_User import Create_User

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Guardian", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS useraccount(UserID VARCHAR(10) PRIMARY KEY,Pin INT)""")

cur.execute("""INSERT INTO useraccount (UserID, Pin) VALUES """)

conn.commit()


cur.close()
conn.close()