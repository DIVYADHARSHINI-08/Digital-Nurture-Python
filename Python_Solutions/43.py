import configparser
class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.filename)

class DatabaseConfig(Config):
    def validate(self):
        required_keys = ["host", "port", "user", "password", "database"]

        if "DATABASE" not in self.config:
            raise Exception("DATABASE section missing in db.ini")

        for key in required_keys:
            if key not in self.config["DATABASE"]:
                raise Exception(f"Missing required key: {key}")

    def display(self):
        db = self.config["DATABASE"]

        print("----- Database Configuration -----")
        print(f"Host     : {db['host']}")
        print(f"Port     : {db['port']}")
        print(f"User     : {db['user']}")
        print(f"Password : {db['password']}")
        print(f"Database : {db['database']}")

try:
    db_config = DatabaseConfig("db.ini")

    db_config.load()
    db_config.validate()
    db_config.display()

except Exception as e:
    print("Error:", e)