import mysql.connector as mysql_connector
from loguru import logger
from mysql.connector import errorcode

from src.Constants import DB_CREDENTIALS_FILE
from src.data.model.serial_device import SerialDevice, Parity
from src.utils.file_operations import file_exists, import_data_from_json

"""
Class to handle database related operations.
"""


class DeviceDatabase:

    def __init__(self):
        self.Error = False
        self.error_msg = ""
        self.table_name = "SerialDevices"
        self.database_name = "serial_device_db"
        if file_exists(DB_CREDENTIALS_FILE):
            data = import_data_from_json(DB_CREDENTIALS_FILE)
            self.connection = self.connect_to_db(host=data["host"], user=data["user"],
                                                 password=data["password"])
            self.cursor = self.connection.cursor()
            self.create_database()
            self.create_device_table()

    def connect_to_db(self, password, host="localhost", user="root"):
        print("Connecting to DB with these parameters", user, host, password)
        try:
            connection = mysql_connector.connect(host=host, user=user, password=password)
            print("Connected to database")
            return connection
        except mysql_connector.Error as e:
            self.Error = True
            print(f"Error: {e}\n")
            if e.errno == errorcode.CR_CONNECTION_ERROR:
                self.error_msg = "Cannot connect to server"
                raise Exception(self.error_msg).with_traceback(e.__traceback__)
            elif e.errno == errorcode.CR_UNKNOWN_HOST:
                self.error_msg = "Cannot connect to the host. Please check if the host is available."
                raise Exception(self.error_msg).with_traceback(e.__traceback__)
            else:
                raise e
        except Exception as e:
            print("Exception", e)

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
                            port_name VARCHAR(50),
                            port VARCHAR(100))
                    """)
        except Exception as e:
            print(e)
            logger.error(e)

    def insert_data(self, data: SerialDevice):
        print("Insert Data", data.device_name)

        def get_parity_char(parity):
            if parity == Parity.NO_PARITY:
                p = "N"
            elif parity == Parity.EVEN:
                p = "E"
            else:
                p = "O"
            return p

        sql = {
            "device_name": data.device_name,
            "product_name": data.product_name,
            "serial_number": data.serial_number,
            "baud_rate": data.baud_rate,
            "parity_bits": get_parity_char(data.parity),
            "data_bits": data.data_bits,
            "port_name": data.port_name,
            "port": data.port
        }

        print(sql)

        add_data = (
            "INSERT INTO SerialDevices (device_name, product_name, serial_number, baud_rate, parity_bits, data_bits, port_name, port)"
            "Values (%(device_name)s, %(product_name)s, %(serial_number)s, %(baud_rate)s, %(parity_bits)s, %(data_bits)s, %(port_name)s, %(port)s)"
        )

        self.cursor.execute(add_data, sql)
        self.connection.commit()

    def get_table_data(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY id DESC")
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(e)
            print(e)

    def update_data(self, device_name, product_name, baud_rate, parity_bits, data_bits, port_name, db_row_id):
        try:
            self.cursor.execute(f"""UPDATE {self.table_name}
                                    SET
                                        device_name = '{device_name}',
                                        product_name = '{product_name}',
                                        baud_rate = {baud_rate},
                                        parity_bits = '{parity_bits}',
                                        data_bits = {data_bits},
                                        port_name = '{port_name}'
                                    WHERE 
                                        id = {db_row_id}
                                """)
        except Exception as e:
            print("Update Error", e)

    def get_table_data_dictionary(self):
        dict_cursor = self.connection.cursor(dictionary=True)
        dict_cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY id DESC")
        results = dict_cursor.fetchall()
        dict_cursor.close()
        return results

    def delete_table(self):
        self.cursor.execute(f"DROP TABLE {self.table_name}")
        self.create_device_table()
        print("DELETED TABLE")

    def delete_database(self):
        self.cursor.execute(f"DROP DATABASE {self.database_name}")
        print("DELETED Database")

    def close_database_connection(self):
        try:
            self.connection.close()
            print("closed")
        except Exception as e:
            logger.error(e)
            print("Connection Close Error: ", e)
