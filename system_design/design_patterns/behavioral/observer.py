from pprint import pprint

class WhatsAppGroup:
    '''
    Subject class
    '''

    def __init__(self):
        self._observers = set() # group memembers

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.phone.messages.append(message)

class Phone:
    def __init__(self):
        self.messages = list()

class Person:
    '''
    Observer class
    '''

    def __init__(self, name, whatsapp_group):
        self.name = name
        self.whatsapp_group = whatsapp_group
        self.phone = Phone()

    def send_text(self, message):
        self.whatsapp_group.notify({self.name: message})

    def read_texts(self):
        pprint(self.phone.messages)

my_whatsapp_group = WhatsAppGroup()

bob = Person('bob', my_whatsapp_group)
lisa = Person('lisa', my_whatsapp_group)
john = Person('john', my_whatsapp_group)

# an admin can control which observers have access
my_whatsapp_group.attach(bob)
my_whatsapp_group.attach(lisa)
my_whatsapp_group.attach(john)

bob.send_text("hey, this is bob")
lisa.send_text("hey, this is lisa")
john.send_text("hey, this is john")

print("lisa's texts:")
lisa.read_texts()