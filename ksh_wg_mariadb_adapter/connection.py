import mysql.connector
from mysql.connector import Error

class DBConnection:
  def __init__(self, connection, debug=False):
    self.connection = connection
    self.debug = debug

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.connection.close()
  
  def test(self):
    try:
        self.connection.cursor().execute("SELECT 1")
        return True, None
    except Error as error:
        return False, str(error)

  def tables(self):
    cursor = self.connection.cursor()
    cursor.execute("SHOW TABLES")
    return [table[0] for table in cursor.fetchall()]

  def sql(self, query):
    if self.debug: print(f"SQL: {query}")

    cursor = self.connection.cursor(dictionary=True)
    cursor.execute(query)

    if query.lower().startswith("select"):
      result = cursor.fetchall()
      return result
    else:
      self.connection.commit()
      return cursor.rowcount

  def select(self, table, where=None, order_by=None, limit=None, project="*"):
    query = f"SELECT {project} FROM {table}"
    if where:
      query += f" WHERE {where}"
    if order_by:
      query += f" ORDER BY {order_by}"
    if limit:
      query += f" LIMIT {limit}"
    
    return self.sql(query)

  def upsert(self, query, row)
    if self.debug: print(f"SQL: {query}")
    values = tuple(row.values())
    cursor = self.connection.cursor()
    try:
      cursor.execute(query, values)
      self.connection.commit()
      return cursor.rowcount
    except Error as error:
      print(f"Error: {error}")
      return None

  def insert(self, table, row):
    columns = ', '.join(row.keys())
    placeholders = ', '.join(['%s'] * len(row))
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    return self.upsert(query, row)

  def update(self, table, row, where=None):
    set_clause = ', '.join([f"{key} = %s" for key in row.keys()])
    query = f"UPDATE {table} SET {set_clause}"

    if where:
      query += f" WHERE {where}"

    return self.upsert(query, row)
    
  def delete(self, table, where=)
    query = f"DELETE FROM {table} WHERE {where}"
    if self.debug: print(f"SQL: {query}")
    cursor = self.connection.cursor()
    try:
      cursor.execute(query)
      self.connection.commit()
      return cursor.rowcount
    
    except Error as error:
      print(f"Error: {error}")
      return None

def connect(host, username, password, database, debug=False):
  try:
    connection = mysql.connector.connect(
      host=host,
      user=username,
      password=password,
      database=database,
      consume_results=True
    )
    if connection.is_connected():
      return DBConnection(connection, debug=debug)

  except Error as error:
    print(f"Error: {error}")
    return None
