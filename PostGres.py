import psycopg2
from Backupbutton import Backupbutton
from Create_User import Create_User

#Connection to the DB
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Guardian", port=5432)

#Create Cursor
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS useraccount(UserID VARCHAR(10) PRIMARY KEY,Pin INT)""")

cur.execute("""INSERT INTO useraccount (UserID, Pin) VALUES )VALUES
(self.UserID, self.Pins)""")

conn.commit()

#Close's the connection
cur.close()
conn.close()