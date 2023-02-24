class ExperianStrategy:
    '''
    Strategy Class
    '''

    @staticmethod
    def get_credit():
        return "experian credit report"

class TransUnionStrategy:
    '''
    Strategy Class
    '''

    @staticmethod
    def get_credit():
        return "transunion credit report"


class Credit:

    def get_credit(self, provider):
        return provider.get_credit()


credit = Credit()

print(credit.get_credit(ExperianStrategy))
print('>> Switching credit provider...')
print(credit.get_credit(TransUnionStrategy))
