import mysql.connector

class DatabaseInitialization():

    def __init__(self, host, user, password):

        self.host = host
        self.user = user
        self.password = password

        self.mysql_connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password)

        self.cnx_cursor = self.mysql_connection.cursor()

        self.database_name = "myCPU_API"

        self.creating_database()
        self.creating_users()
        self.creating_tables()

    def creating_database(self):
        create_description = (f"CREATE DATABASE {self.database_name}")

        try:
            self.cnx_cursor.execute(create_description)
        except mysql.connector.Error as error:
            print(error)

        self.cnx_cursor.execute(f'USE {self.database_name};')

    def creating_users(self):
        USERS = {}
        PRIVILEGES = {}
        
        USERS['reader'] = (f"CREATE USER 'reader'@'{self.host}';")
        PRIVILEGES['reader'] = (f"GRANT SELECT ON {self.database_name}.* TO 'reader'@'{self.host}';")
                            
        USERS['publisher'] = (f"CREATE USER 'publisher'@'{self.host}'")
        PRIVILEGES['publisher'] = (f"GRANT INSERT ON {self.database_name}.* TO 'publisher'@'{self.host}'")
        
        for user in USERS:
            user_descripton = USERS[user]

            try:
                self.cnx_cursor.execute(user_descripton)
            except mysql.connector.Error as error:
                print(error)

        for privilege in PRIVILEGES:
            privilege_description = PRIVILEGES[privilege]

            try:
                self.cnx_cursor.execute(privilege_description)
            except mysql.connector.Error as error:
                print(error)

    def creating_tables(self):
        TABLES = {}

        #gpu table
        TABLES['gpu_infos'] = (
            "CREATE TABLE `gpu_infos` ("
            "  `gpu_name` varchar(50) NOT NULL,"
            "  `gpu_vram_total_gb` varchar(4) NOT NULL,"
            "  `gpu_vram_usage_gb` varchar(4) NOT NULL,"
            "  `gpu_temperature_celcius` float NOT NULL,"
            "  `gpu_power_watts` smallint NOT NULL,"
            "  `gpu_usage_percent` smallint NOT NULL,"
            "  `datetime` datetime NOT NULL)"
            )

        #cpu table
        TABLES['cpu_infos'] = (
            "CREATE TABLE `cpu_infos` ("
            "  `cpu_name` varchar(50) NOT NULL,"
            "  `cpu_percent` float NOT NULL,"
            "  `cpu_freq` smallint NOT NULL,"
            "  `datetime` datetime NOT NULL)"
            )

        #mem ram table
        TABLES['mem_ram_info'] = (
            "CREATE TABLE `mem_ram_infos` ("
            "  `total_mem` varchar(5) NOT NULL,"
            "  `available_mem` varchar(5) NOT NULL,"
            "  `active_mem` varchar(5) NOT NULL,"
            "  `percent_mem` float NOT NULL,"
            "  `datetime` datetime NOT NULL)"
            )

        #motherboard tables
        TABLES['motherboard_infos'] = (
            "CREATE TABLE `motherboard_infos` ("
            "  `motherboard_manufacturer` varchar(50) NOT NULL,"
            "  `motherboard_model_name` varchar(50) NOT NULL,"
            "  `datetime` datetime NOT NULL)"
            )

        for table in TABLES:
            table_description = TABLES[table]

            try:
                self.cnx_cursor.execute(table_description)
            except mysql.connector.Error as error:
                print(error)

    def return_cursor(self):
        return self.cnx_cursor

DatabaseInitialization('YOUR HOST','YOUR USER','YOUR USER PASSWORD')