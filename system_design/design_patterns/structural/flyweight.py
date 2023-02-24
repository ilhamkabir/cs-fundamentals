import sys

class EphemeralDatabaseManager:
    '''
    Flyweight Class

    Stores the intrsinsic state of the object
    '''

    DB_NAME = "PostgreSQL"

    def clear(self):
        '''
        Run if the database is getting full
        '''
        print('clear db')

    def backup(self):
        print('backup db')

class LoadBalancerManager:
    '''
    Flyweight Class

    Stores the intrsinsic state of the object
    '''

    LOAD_BALANCER_NAME = "Elastic Beanstalk"

    def launch_server(self):
        print('launch new server')

    def destroy_server(self):
        print('destroy a server')

    def assign_task(self):
        print('assign_server_a_task')
    
class FlyWeightFactory:

    obj_store = dict() # {class_name:obj} | type: {str:obj}

    def get_flyweight(self, key):
        if key in FlyWeightFactory.obj_store:
            return FlyWeightFactory.obj_store[key]
        else:
            specific_service_class = getattr(sys.modules[__name__], key)
            specific_service_obj = specific_service_class()
            FlyWeightFactory.obj_store[key] = specific_service_obj
            return specific_service_obj


fly_weight_factory = FlyWeightFactory()
db_manager = fly_weight_factory.get_flyweight("EphemeralDatabaseManager")

db_manager.clear()

new_db_manager = fly_weight_factory.get_flyweight("EphemeralDatabaseManager")

print("both db managers are the same?:", db_manager is new_db_manager)