# Builder Pattern

class Computer:
    '''
    Product Class: The end goal is to have instances of this object
    '''
    pass

class ComputerBuilder:
    '''
    Builder Class: Has functions to add parts of to the Product object
    '''

    def new_computer(self):
        self._computer = Computer()

    def get_computer(self):
        return self._computer

    def get_case(self):
        self._computer.case = 'Corsair'
     
    def install_mainboard(self):
        self._computer.mainboard = 'ASUS'
        self._computer.cpu = 'AMD'
        self._computer.memory = '2 X 4GB'

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate'

    def install_video_card(self):
        self._computer.video_card = 'On board'

    def install_fan(self):
        self._computer.fan = 'Airflow'

class Director:
    '''
    Director Class: Constructs/retrieves an unique representation of Product
    '''

    def __init__(self, builder):
        self._builder = builder

    def build_cheap_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def build_gaming_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()
        self._builder.install_fan()

    def get_computer(self):
        return self._builder.get_computer()


director = Director(ComputerBuilder())

cheap_computer = director.build_cheap_computer()
gaming_computer = director.build_gaming_computer()

print(cheap_computer.case)
print(gaming_computer.mainboard)
