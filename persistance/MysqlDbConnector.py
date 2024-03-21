import mysql.connector
from mysql.connector import Error

class MySQLRepository:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def execute_query(self, query, params=None):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            connection.commit()
            return cursor.fetchall()

        except Error as e:
            print(f"Error executing query: {e}")
            return None

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Example usage:
host = "jamshid.mysql.database.azure.com"
user = "jamshid"
password = "Eftekhar2024!"
database = "orderdb"


repository = MySQLRepository(host, user, password, database)

# Example: Execute a query to retrieve all rows from a table
query = "SELECT * FROM orders"
rows = repository.execute_query(query)
print("Rows:", rows)

# Example: Execute a query with parameters
#query = "SELECT * FROM your_table WHERE order_id = %s"
#params = ("value", 1001)
#rows_with_params = repository.execute_query(query, params)
#print("Rows with params:", rows_with_params)
