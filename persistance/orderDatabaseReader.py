import sqlite3

class OrderDatabaseReader:
    def __init__(self, db_path):
        self.db_path = db_path

    def read_orders(self, columns="*", condition=""):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Construct the SQL query
            query = f"SELECT {columns} FROM orders"
            if condition:
                query += f" WHERE {condition}"

            # Retrieve data from the 'orders' table
            cursor.execute(query)
            data = cursor.fetchall()

            return data

        except sqlite3.Error as e:
            print(f"Error reading order data from the database: {e}")
            return None

        finally:
            if connection:
                connection.close()

    def read_orders_with_details(self, columns="*", condition=""):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Construct the SQL query to join 'orders' with 'vat' and 'discount' tables
            query = f"SELECT {columns} FROM orders " \
                    f"JOIN vat ON orders.vat_id = vat.vat_id " \
                    f"JOIN discount ON orders.discount_id = discount.discount_id"
            if condition:
                query += f" WHERE {condition}"

            # Retrieve data from the joined tables
            cursor.execute(query)
            data = cursor.fetchall()

            return data

        except sqlite3.Error as e:
            print(f"Error reading order data with details from the database: {e}")
            return None

        finally:
            if connection:
                connection.close()

# Example usage:
db_path = "order_database.db"  # Replace with your SQLite database path

order_reader = OrderDatabaseReader(db_path)

# Read all orders with VAT rate and discount rate
all_orders_with_details = order_reader.read_orders_with_details()
print("All Orders with Details:", all_orders_with_details)

# Read orders with details for a specific customer (replace 'CustomerID' and '1' with your desired condition)
customer_orders_with_details = order_reader.read_orders_with_details(condition="order_id = 1")
print("Customer Orders with Details:", customer_orders_with_details)

