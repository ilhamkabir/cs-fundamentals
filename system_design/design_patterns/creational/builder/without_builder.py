# Without Builder Pattern

class Computer:
    '''
    To create any instance of Computer, we need to
    pass a value for every initialization argument.
    '''

    def __init__(
        self, 
        case, 
        mainboard, 
        cpu, 
        memory, 
        hard_drive, 
        video_card,
        fan
    ):
        self.case       = case
        self.mainboard  = mainboard
        self.cpu        = cpu # sometimes a part of the mainboard.
        self.memory     = memory # sometimes a part of the mainboard.
        self.hard_drive = hard_drive
        self.video_card = video_card
        self.fan        = fan

cheap_computer = Computer(
    case        = 'Coolermaster',
    mainboard   = 'MSI',
    cpu         = 'Intel Core i9',
    memory      = '2 X 16GB',
    hard_drive  = 'SSD 2TB',
    video_card  = None # need a val even if i don't want a video card
    fan         = None
)

print(cheap_computer.case)
print(cheap_computer.mainboard)
print(cheap_computer.cpu)

