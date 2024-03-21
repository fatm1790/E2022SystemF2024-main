import mysql.connector
from mysql.connector import Error

class DatabaseReader:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def read_data(self, table_name, columns="*", condition=""):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            # Construct the SQL query
            query = f"SELECT {columns} FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"

            # Retrieve data from the specified table
            cursor.execute(query)
            data = cursor.fetchall()

            return data

        except Error as e:
            print(f"Error reading data from the database: {e}")
            return None

        finally:
            if connection.is_connected():
                connection.close()

class CustomerDataReader(DatabaseReader):
    def read_customers(self, columns="*", condition=""):
        return self.read_data("Customers", columns, condition)

class EmployeeDataReader(DatabaseReader):
    def read_employees(self, columns="*", condition=""):
        return self.read_data("Employees", columns, condition)

class VendorDataReader(DatabaseReader):
    def read_vendors(self, columns="*", condition=""):
        return self.read_data("Vendors", columns, condition)

class ProductDataReader(DatabaseReader):
    def read_products(self, columns="*", condition=""):
        return self.read_data("Products", columns, condition)

# Example usage:
# Example usage:
# host = "localhost"
# user = "root"
# password = "jam2003eft"
# database = "salesordersdelivery"

host = "mysql78.unoeuro.com"
user = "jaef_dk"
password = "e49Dh25cdnGpkgFy6rEB"
database = "jaef_dk_db"

customer_reader = CustomerDataReader(host, user, password, database)
employee_reader = EmployeeDataReader(host, user, password, database)
vendor_reader = VendorDataReader(host, user, password, database)
product_reader = ProductDataReader(host, user, password, database)

# Read data for customers, employees, vendors, and products
customers_data = customer_reader.read_customers()
employees_data = employee_reader.read_employees()
vendors_data = vendor_reader.read_vendors()
products_data = product_reader.read_products()

# Print or process the retrieved data as needed
print("Customers:", customers_data)
print("Employees:", employees_data)
print("Vendors:", vendors_data)
print("Products:", products_data)
