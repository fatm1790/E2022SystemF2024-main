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

            if cursor.description is not None:  # Check if the query returned any rows
                rows = cursor.fetchall()
            else:
                rows = None

            connection.commit()
            return rows


        except Error as e:
            print(f"Error executing query: {e}")
            return None

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Example usage:
host = "sqlkea.mysql.database.azure.com"
user = "fatmamustafa"
password = "Sommer123123!"
database = "orderdb"



repository = MySQLRepository(host, user, password, database)

# # Example: Execute a query to retrieve all rows from a table
# query = "SELECT * FROM vat"
# rows = repository.execute_query(query)
# print("Rows:", rows)

# # Example: Execute a query with parameters
# query = "SELECT * FROM vat WHERE VAT_ID = %s"
# params = (5,)  # Assuming you want to retrieve rows where VAT_ID is 5
# rows_with_params = repository.execute_query(query, params)
# print("Rows with params:", rows_with_params)

# # Example: Fetch all VAT data from the database
# query = "SELECT * FROM vat"
# vat_data = repository.execute_query(query)

# # Display the VAT data
# if vat_data:
#     print("VAT Data:")
#     for row in vat_data:
#         print(row)  # Assuming each row is a tuple representing a record
# else:
#     print("No VAT data found.")



import matplotlib.pyplot as plt

# Example: Fetch all VAT data from the database
query = "SELECT * FROM vat"
vat_data = repository.execute_query(query)

# Extracting VAT rates and corresponding countries
countries = []
vat_rates = []

if vat_data:
    for row in vat_data:
        countries.append(row[1])  # Assuming country is the second column (index 1)
        vat_rates.append(row[3])   # Assuming VAT rate is the fourth column (index 3)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(countries, vat_rates, color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('VAT Rate (%)')
    plt.title('VAT Rates by Country')
    plt.xticks(rotation=45, ha='right')  # Rotate country names for better readability
    plt.tight_layout()
    plt.show()
else:
    print("No VAT data found.")
