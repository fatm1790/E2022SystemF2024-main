from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt


class OrderDataReader:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def read_order_dates(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            # Retrieve data from the 'Orders' table
            cursor.execute("SELECT OrderDate FROM Orders")
            data = cursor.fetchall()

            return data

        except Error as e:
            print(f"Error reading order dates from the database: {e}")
            return None

        finally:
            if connection.is_connected():
                connection.close()

    def create_bar_chart(self, data, interval):
        if not data:
            print("No data available to create a bar chart.")
            return

        order_dates = [date[0] for date in data]
        grouped_dates = self.group_dates(order_dates, interval)

        date_counts = {date: grouped_dates.count(date) for date in set(grouped_dates)}

        dates, counts = zip(*sorted(date_counts.items()))

        plt.bar(dates, counts, color='blue')
        plt.xlabel(f'Order Date ({interval.capitalize()})')
        plt.ylabel('Number of Orders')
        plt.title(f'Number of Orders by {interval.capitalize()}')
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def group_dates(self, dates, interval):
        grouped_dates = []

        for date in dates:
            if interval == 'weekly':
                week_start = date - timedelta(days=date.weekday())
                grouped_dates.append(week_start)
            elif interval == 'monthly':
                month_start = date.replace(day=1)
                grouped_dates.append(month_start)

        return grouped_dates
    

# Example usage:
# host = "localhost"
# user = "root"
# password = "jam2003eft"
# database = "salesordersdelivery"

host = "mysql78.unoeuro.com"
user = "jaef_dk"
password = "e49Dh25cdnGpkgFy6rEB"
database = "jaef_dk_db"

order_reader = OrderDataReader(host, user, password, database)

order_dates_data = order_reader.read_order_dates()

if order_dates_data:
    # Specify the interval ('weekly' or 'monthly')
    interval = 'weekly'
    order_reader.create_bar_chart(order_dates_data, interval)
