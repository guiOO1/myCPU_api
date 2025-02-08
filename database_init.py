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

    def creating_database(self):
        create_description = (f"CREATE DATABASE {self.database_name}")

        try:
            self.cnx_cursor.execute(create_description)
        except mysql.connector.Error as error:
            print(error)

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

        #gpu tables
        TABLES['gpu_name'] = ()

        TABLES['gpu_mem_info'] = ()

        TABLES['gpu_vram_usage'] = ()

        TABLES['gpu_temperature'] = ()

        TABLES['gpu_power'] = ()

        TABLES['gpu_usage'] = ()

        #cpu tables
        TABLES['cpu_name'] = ()

        TABLES['cpu_percent'] = ()

        TABLES['cpu_freq'] = ()

        #mem ram tables
        TABLES['total_mem'] = ()

        TABLES['available_mem'] = ()

        TABLES['active_mem'] = ()

        TABLES['active_mem'] = ()

        #motherboard tables
        TABLES['motherboard_manufacturer'] = ()

        TABLES['motherboard_model_name'] = ()

        for table in TABLES:
            table_description = TABLES[table]

            try:
                self.cnx_cursor.execute(table_description)
            except mysql.connector.Error as error:
                print(error)

DatabaseInitialization(0,0,0)