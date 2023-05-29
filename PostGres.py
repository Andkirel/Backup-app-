import psycopg2
from Backupbutton import Backupbutton


class PostGres:

 global conn
 global cur

 conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Guardian", port=5432)

#Create Cursor
 cur = conn.cursor()

 cur.execute("""CREATE TABLE IF NOT EXISTS useraccount(UserID VARCHAR(10) PRIMARY KEY,Pin INT)""")
 conn.commit()

 def AddUser(UserID: str, Pin: int) -> bool:

  if UserID and Pin:
   cur.execute(f"INSERT INTO useraccount (UserID, Pin)VALUES(?,?)",
   ('{UserID}', '{Pins}'))
   conn.commit()

   return True
  else: return False

 conn.commit()

#Close's the connection
 cur.close()
 conn.close()