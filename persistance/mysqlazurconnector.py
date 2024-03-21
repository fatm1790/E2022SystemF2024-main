import mysql.connector

# Define connection parameters
config = {
    'user': 'jamshid',
    'password': 'Eftekhar2024!',
    'host': 'jamshid.mysql.database.azure.com',
    'database': 'orderdb',
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'  # Path to SSL CA certificate file (required for SSL connection)
}

# Establish connection
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()

        # Example query
        query = "SELECT * FROM orders"

        # Execute query
        cursor.execute(query)

        # Fetch data
        data = cursor.fetchall()

        for row in data:
            print(row)

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
