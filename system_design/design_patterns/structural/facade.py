class Salesforce:
    '''
    Only save ints to Salesforce!!
    '''

    @staticmethod
    def save(data):
        print('save to salesforce')

class MySQL:
    '''
    Only save strings to MySQL!!
    '''
    
    @staticmethod
    def save(data):
        print('save to mysql')

class PSQL:
    '''
    Only save lists to PostgreSQL!!
    '''

    @staticmethod
    def save(data):
        print('save to postgres')

class DatabaseFacade:

    @staticmethod
    def save(data):
        if isinstance(data, int):
            Salesforce.save(data)
        elif isinstance(data, str):
            MySQL.save(data)
        elif isinstance(data, list):
            PSQL.save(data)
        else:
            raise ValueError

DatabaseFacade.save(5)
