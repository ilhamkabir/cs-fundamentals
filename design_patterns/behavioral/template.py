import abc

class AbcReport(abc.ABC):

    def generate_and_send(self):
        self.get_data()
        self.generate()
        self.save()
        self.send()

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def generate(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def send(self):
        pass

class DisbursementReport(AbcReport):

    def get_data(self):
        print('get data')

    def generate(self):
        print('generate report')

    def save(self):
        print('save report')

    def send(self):
        print('send report')

disbursement_report = DisbursementReport()
disbursement_report.generate_and_send()
