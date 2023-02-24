class PostgreSQL:

    def save(self):
        print('save to pgsql')

class MySQL:

    def save(self):
        print('save to mysql') 

pgsql = PostgreSQL()
mysql = MySQL()

pgsql.save()
mysql.save()

print('--------')

class Mediator:

    def __init__(self):
        self.pgsql = PostgreSQL()
        self.mysql = MySQL()

    def save_to_pgsql(self):
        print('save to pgsql')

    def save_to_mysql(self):
        print('save to mysql') 

mediator = Mediator()
mediator.save_to_pgsql()
mediator.save_to_mysql()
