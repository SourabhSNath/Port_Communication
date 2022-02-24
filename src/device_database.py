import mysql.connector as mysql_connector
from mysql.connector import errorcode


class DeviceDatabase:

    def __init__(self):
        self.Error = False
        self.error_msg = ""
        self.table_name = "SerialDevices"
        self.database_name = "serial_device_db"
        try:
            self.connection = mysql_connector.connect(host="localhost", user="root", password="test_password")
            self.cursor = self.connection.cursor()
            print("Connected to database")
        except mysql_connector.Error as e:
            self.Error = True
            print(f"Error: {e}\n")
            if e.errno == errorcode.CR_CONNECTION_ERROR:
                self.error_msg = "Cannot connect to server"
                print(self.error_msg, e)
            elif e.errno == errorcode.CR_UNKNOWN_HOST:
                self.error_msg = "Cannot connect to the host. Please check if the host is available."
                print(self.error_msg, e)
            else:
                self.error_msg = f"Unknown error. {e}"
                print(e)
        self.create_database()
        self.create_device_table()

    # Create Database if it does not exist
    def create_database(self):
        if not self.Error:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
            self.cursor.execute(f"USE {self.database_name}")
            print("Create Database")
        else:
            print("Error")

    # Create table if it does not exist.
    # Port name is optional because linux and windows use different port names. The user chooses if it needs to be
    # added to the db.
    # parity_bits ENUM('NO Parity', 'EVEN', 'ODD') NOT NULL ???
    def create_device_table(self):
        try:
            self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS SerialDevices (
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            device_name TEXT NOT NULL,
                            product_name TEXT NOT NULL,
                            serial_number VARCHAR(255) NOT NULL,
                            baud_rate MEDIUMINT UNSIGNED NOT NULL,
                            parity_bits CHAR(1) NOT NULL,
                            data_bits SMALLINT NOT NULL,
                            port_name VARCHAR(50))
                    """)
            self.cursor.execute(f"Describe {self.table_name}")
            for x in self.cursor:
                print(x)
        except Exception as e:
            print(e)

    def insert_data(self, device_name, product_name, serial_number, baud_rate, parity_bits, data_bits, port_name):
        if not device_name:
            device_name = product_name
        sql = f""" 
                INSERT INTO {self.table_name} (device_name, product_name, serial_number, baud_rate, parity_bits, data_bits, port_name)
                VALUES ('{device_name}', '{product_name}', '{serial_number}', {baud_rate}, '{parity_bits}', {data_bits}, '{port_name}')              
            """
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()

    def get_table_data(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY id DESC")
        return self.cursor.fetchall()

    def delete_database(self):
        self.cursor.execute(f"DROP DATABASE {self.database_name}")
        print("DELETED Database")

    def close_database_connection(self):
        self.connection.close()
