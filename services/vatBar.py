import sqlite3
import matplotlib.pyplot as plt

class VatDataReader:
    def __init__(self, db_path):
        self.db_path = db_path

    def read_data(self):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Retrieve data from the 'vat' table
            cursor.execute("SELECT country_code, vat_rate FROM vat")
            data = cursor.fetchall()

            return data

        except sqlite3.Error as e:
            print("Error reading data from the database:", e)
            return None

        finally:
            if connection:
                connection.close()

    def create_bar_chart(self, data):
        if not data:
            print("No data available to create a bar chart.")
            return

        country_codes, vat_rates = zip(*data)

        plt.bar(country_codes, vat_rates, color='blue')
        plt.xlabel('Country Code')
        plt.ylabel('VAT Rate (%)')
        plt.title('VAT Rates by Country')
        plt.show()

# Example usage:
db_path = "./persistance/order_database.db"  # Update with your database path
vat_reader = VatDataReader(db_path)

vat_data = vat_reader.read_data()

if vat_data:
    vat_reader.create_bar_chart(vat_data)
