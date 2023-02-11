import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("c:/Users/yaro/Desktop/MyFirstFramework/test_database.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        version = self.cursor.fetchall()
        print("SQLite version:", version)

    def get_all_users(self):
        self.cursor.execute(
            "SELECT first_name, last_name, address, city \
            FROM customers;"
        )
        return self.cursor.fetchall()

    def get_user_address_by_name(self, first_name, last_name):
        self.cursor.execute(
            f"SELECT address, city, postal_code, country \
            FROM customers \
            WHERE first_name = '{first_name}' AND last_name = '{last_name}';"
        )
        return self.cursor.fetchall()

    def update_product_qnt_by_id(self, product_id, qnt):
        self.cursor.execute(
            f"UPDATE products SET quantity = {qnt} WHERE id = {product_id};"
        )
        self.connection.commit()
        

    def select_product_qnt_by_id(self, product_id):
        self.cursor.execute(
            f"SELECT quantity FROM products WHERE id = {product_id};"
        )
        return self.cursor.fetchall()

    def insert_product(self, product_id, name, description, qnt):
        self.cursor.execute(
            f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES \
            ({product_id}, '{name}', '{description}', {qnt});"
        )
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        self.cursor.execute(
            f"DELETE FROM products WHERE id = {product_id};"
        )
        self.connection.commit()

    def get_detailed_orders(self):
        self.cursor.execute(
            "SELECT orders.id, first_name, last_name, name, description, order_date \
            FROM orders \
            JOIN customers \
            ON orders.customer_id = customers.id \
            JOIN products \
            ON orders.product_id = products.id;"
        )
        return self.cursor.fetchall()
