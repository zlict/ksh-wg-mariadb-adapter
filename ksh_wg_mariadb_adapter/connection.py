import mysql.connector
from mysql.connector import Error

class DBConnection:
  def __init__(self, connection):
    self.connection = connection

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.connection.close()
  
  def test(self):
    try:
        self.connection.cursor().execute("SELECT 1")
        return True, None
    except Error as e:
        return False, str(e)

  def tables(self):
    cursor = self.connection.cursor()
    cursor.execute("SHOW TABLES")
    return [table[0] for table in cursor.fetchall()]

  def sql(self, query):
    cursor = self.connection.cursor(dictionary=True)
    cursor.execute(query)
    print(f"SQL: {query}")

    try: 
      if query.lower().startswith("select"):
          result = cursor.fetchall()
          return result
      else:
          self.connection.commit()
          return cursor.rowcount

    except mysql.connector.errors.InterfaceError as error:
      if error.msg == 'No result set to fetch from.':
          pass
      else:
          raise 
      

  def select(self, table, where=None, order_by=None, limit=None, project="*"):
    query = f"SELECT {project} FROM {table}"
    if where:
        query += f" WHERE {where}"
    if order_by:
        query += f" ORDER BY {order_by}"
    if limit:
        query += f" LIMIT {limit}"
    
    return self.sql(query)

def connect(host, username, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            consume_results=True
        )
        if connection.is_connected():
            return DBConnection(connection)
    except Error as e:
        print(f"Error: {e}")
        return None
