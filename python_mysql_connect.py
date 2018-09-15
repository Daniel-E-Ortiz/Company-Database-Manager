from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def connect():
  """ Connect to MySQL database """

  db_config = read_db_config()

  try:
    print('Connecting to MySQL database...')
    cnx = MySQLConnection(**db_config)
    cursor = cnx.cursor()
    
    if cnx.is_connected():
      print('Connection established.')
      cursor.execute('SELECT * FROM customers ORDER BY customerName')
      row = cursor.fetchone()

      while row is not None:
        print(row)
        row = cursor.fetchone()
        
    else:
      print('Connection failed.')

  except Error as error:
    print(error)

  finally:
    cursor.close()
    cnx.close()
    print('Connection closed.')
    
if __name__ == '__main__':
  connect()
