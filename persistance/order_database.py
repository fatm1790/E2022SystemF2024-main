import sqlite3

import sqlite3

def create_database():
    connection = sqlite3.connect("order_database.db")
    cursor = connection.cursor()

    # Create 'vat' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS vat
                      (vat_id INTEGER PRIMARY KEY,
                       country_code TEXT,
                       vat_rate REAL)''')

    # Create 'discount' table with 'order_value' attribute
    cursor.execute('''CREATE TABLE IF NOT EXISTS discount
                      (discount_id INTEGER PRIMARY KEY,
                       discount_rate REAL,
                       order_value REAL)''')

    # Create 'orders' table with foreign keys
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                      (order_id INTEGER PRIMARY KEY, 
                       item_name TEXT,
                       quantity INTEGER,
                       unit_price REAL,
                       vat_id INTEGER,
                       discount_id INTEGER,
                       FOREIGN KEY (vat_id) REFERENCES vat(vat_id),
                       FOREIGN KEY (discount_id) REFERENCES discount(discount_id))''')

    connection.commit()
    return connection, cursor

# Rest of the code remains unchanged...


def add_order_to_database(connection, cursor, item_name, quantity, unit_price, vat_id, discount_id):
    """
    Add order information to the SQLite 'orders' table.

    Parameters:
    - connection: SQLite database connection.
    - cursor: SQLite database cursor.
    - item_name: Name of the item.
    - quantity: Quantity of the item.
    - unit_price: Unit price of the item.
    - vat_id: ID of the VAT rate from the 'vat' table.
    - discount_id: ID of the discount rate from the 'discount' table.
    """
    cursor.execute('''INSERT INTO orders (item_name, quantity, unit_price, vat_id, discount_id) 
                      VALUES (?, ?, ?, ?, ?)''', (item_name, quantity, unit_price, vat_id, discount_id))
    connection.commit()

def add_vat_to_database(connection, cursor, country_code, vat_rate):
    """
    Add VAT information to the SQLite 'vat' table.

    Parameters:
    - connection: SQLite database connection.
    - cursor: SQLite database cursor.
    - country_code: The country code.
    - vat_rate: The VAT rate for the specified country in Europe.
    """
    cursor.execute("INSERT OR REPLACE INTO vat (country_code, vat_rate) VALUES (?, ?)",
                   (country_code, vat_rate))
    connection.commit()

def add_discount_to_database(connection, cursor, discount_rate, order_value):
    """
    Add discount information to the SQLite 'discount' table.

    Parameters:
    - connection: SQLite database connection.
    - cursor: SQLite database cursor.
    - discount_rate: The discount rate.
    """
    cursor.execute("INSERT OR REPLACE INTO discount (discount_rate, order_value) VALUES (?, ?)", (discount_rate, order_value))
    connection.commit()

def close_database(connection):
    """
    Close the SQLite database connection.

    Parameters:
    - connection: SQLite database connection.
    """
    connection.close()

# Example usage:
try:
    connection, cursor = create_database()

    # Adding VAT and discount information to the database
    add_vat_to_database(connection, cursor, "DE", 19.0)
    add_vat_to_database(connection, cursor, "FR", 20.0)
    add_vat_to_database(connection, cursor, "IT", 22.0)
    add_vat_to_database(connection, cursor, "ES", 21.0)
    add_vat_to_database(connection, cursor, "GB", 20.0)
    add_vat_to_database(connection, cursor, "PL", 23.0)
    add_vat_to_database(connection, cursor, "RO", 19.0)
    add_vat_to_database(connection, cursor, "NL", 21.0)
    add_vat_to_database(connection, cursor, "BE", 21.0)
    add_vat_to_database(connection, cursor, "EL", 24.0)
    add_vat_to_database(connection, cursor, "CZ", 21.0)
    add_vat_to_database(connection, cursor, "PT", 23.0)
    add_vat_to_database(connection, cursor, "HU", 27.0)
    add_vat_to_database(connection, cursor, "SE", 25.0)
    add_vat_to_database(connection, cursor, "AT", 20.0)
    add_vat_to_database(connection, cursor, "BG", 20.0)
    add_vat_to_database(connection, cursor, "DK", 25.0)

    add_discount_to_database(connection, cursor, 1000.0, 3)
    add_discount_to_database(connection, cursor, 5000.0, 5)
    add_discount_to_database(connection, cursor, 7000.0, 7)
    add_discount_to_database(connection, cursor, 10000.0, 10)

    # Getting VAT and discount IDs for an order
    cursor.execute("SELECT vat_id FROM vat WHERE country_code = 'DE'")
    vat_id = cursor.fetchone()[0]

    cursor.execute("SELECT discount_id FROM discount")
    discount_id = cursor.fetchone()[0]

    # Adding an order to the database
    add_order_to_database(connection, cursor, "ProductA", 5, 15.99, vat_id, discount_id)
    add_order_to_database(connection, cursor, "ProductB", 2, 10.99, vat_id, discount_id)

    # Retrieving order information from the database
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    for order in orders:
        print(f"Order ID: {order[0]}, Item: {order[1]}, Quantity: {order[2]}, Unit Price: {order[3]}, "
              f"VAT ID: {order[4]}, Discount ID: {order[5]}")

finally:
    close_database(connection)
