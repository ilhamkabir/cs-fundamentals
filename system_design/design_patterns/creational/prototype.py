import copy

class JobApplication:
    
    def __init__(self, company, personal_info, work_experience, education):
        self.company = company
        self.personal_info = personal_info
        self.work_experience = work_experience
        self.education = education

    def send(self):
        print("Sending job app to {}".format(self.company))

    def deep_copy(self):
        '''
        This is what makes JobApplicaiton a Prototype Class.
        '''
        return copy.deepcopy(self)

def complex_operation():
    pass

print(">> Create job applications for Apple and Google.\n------------")

apple = JobApplication(
    company         = "Apple",
    personal_info   = "blah blah",
    work_experience = "blah blah",
    education       = "blah blah"
)
print(">> Send Apple job app.")
apple.send()

google = JobApplication(
    company         = "Google",
    personal_info   = "blah blah",
    work_experience = "blah blah",
    education       = "blah blah"
)
print(">> Send Google job app.")
google.send()

print(">> Create a deep copy of Google job app.")
amazon = google.deep_copy()
amazon.company = "Amazon"

print(">> Send Amazon job app.")
amazon.send()

