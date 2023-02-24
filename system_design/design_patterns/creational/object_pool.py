class DBConnection:

    def __init__(self):
        print('Running complex operations to establish a DB connection.')

class DBConnectionPool:
    '''
    ObjectPool Class
    '''

    def __init__(self):
        # pool of objects
        self._connections = [
            DBConnection(),
            DBConnection()
        ]

    def get_connection(self):
        # first check if any objects are available in the pool
        if len(self._connections) > 0:
            connection = self._connections.pop() # removes a connection from the pool
            print('Returning Connection')
            return connection
        else:
            # if the pool is empty
            print("No connections available.")

    def release_connection(self, connection):
        print("Releasing Connection")
        self._connections.append(connection)


print('>> Create the object pool with 2 connections.')
object_pool = DBConnectionPool()

print('>> Bob and Lisa both want connections.')
bobs_connection = object_pool.get_connection()
lisas_connection = object_pool.get_connection()

print('>> John keeps trying to get a connection, but none are available.')
johns_connection = object_pool.get_connection()
johns_connection = object_pool.get_connection()
johns_connection = object_pool.get_connection()
johns_connection = object_pool.get_connection()
johns_connection = object_pool.get_connection()

print('>> Bob is releasing his connection.')
object_pool.release_connection(bobs_connection)

print('>> Now John can get his connection.')
johns_connection = object_pool.get_connection()
