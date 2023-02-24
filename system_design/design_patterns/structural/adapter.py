import abc

class AbcReport(abc.ABC):

    @abc.abstractmethod
    def generate(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def send_to_pheaa(self):
        pass

class PheaaReport(AbcReport):
    def generate(self):
        print('generated report')

    def save(self):
        print('saved report')

    def send_to_pheaa(self):
        print('sent to pheaa')

class BlmAdapter(AbcReport):

    @abc.abstractmethod
    def send_to_blm(self):
        pass

    def send_to_pheaa(self):
        self.send_to_blm()

class BlmReport(BlmAdapter):
    def generate(self):
        print('generated report')

    def save(self):
        print('saved report')

    def send_to_blm(self):
        print('sent to blm')

blm_report = BlmReport()
blm_report.send_to_pheaa()
