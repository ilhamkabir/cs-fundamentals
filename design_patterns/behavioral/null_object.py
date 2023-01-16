class NullClass:
    def backup(self):
        print("program didn't break")

class PostgreSQL:
    def backup(self):
        print("backup pgsql")

class MySQL:
    def backup(self):
        print("backup mysql")

class Mongo:
    def backup(self):
        print("backup mongo")

class DBFactory:

    @staticmethod
    def get_database(db_name):
        '''
        MongoDB isn't use anymore.
        '''
        if db_name == "PostgreSQL":
            return PostgreSQL()
        elif db_name == "MySQL":
            return MySQL()
        # elif db == "Mongo":
        #     return Mongo()
        else:
            return NullClass()

for db_name in ['PostgreSQL', 'MySQL', 'Mongo']:
    db = DBFactory.get_database(db_name)
    db.backup()

