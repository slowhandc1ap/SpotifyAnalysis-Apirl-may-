import mysql.connector  
from mysql.connector import Error

conn = mysql.connector.connect(
      host='localhost',
      database = 'spotify',
      user='root',
      password=''
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE song (name varchar(20) , artis varchar(50))")