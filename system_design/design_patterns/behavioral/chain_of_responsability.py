class FederalHousingAdministration:

    @staticmethod
    def handle_request():
        print("Step 1: FHA picks homes they'll insure")

class FederalHousingFinanceAgency:

    @staticmethod
    def handle_request():
        print('Step 2: FHFA sets loan limits & underwriting guidelines')

class Customer:

    @staticmethod
    def handle_request():
        print('Step 3: Customer applies for a mortgage')

class Bank:

    @staticmethod
    def handle_request():
        print('Step 4: Bank provide compliant loan')

class FannieMae:

    @staticmethod
    def handle_request():
        print('Step 5: GSE purchases loan & securitizes them')

class Investor:

    @staticmethod
    def handle_request():
        print('Step 6: Investor purchases loan security')

for party in [
    FederalHousingAdministration,
    FederalHousingFinanceAgency,
    Customer,
    Bank,
    FannieMae,
    Investor
]:
    party.handle_request()



