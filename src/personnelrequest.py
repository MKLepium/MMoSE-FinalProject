import itertools

class PersonnelRequest:
    newid = itertools.count()
        
    def __init__(self):
        self.jobtitle = input("What is the title of the Job: ")
        self.jobdesc = input("Give a brief description of the job: ")
        self.deadline = input("When is this deadline for this personnel request: ")
        self.id = next(PersonnelRequest.newid)
    def __repr__(self):
        return "Id: " + str(self.id) + "\nJobtitle: "+ self.jobtitle + "\nJobdescription: " + self.jobdesc + "\nDeadline: " + str(self.deadline)
    def __str__(self):
        return "Id: " + str(self.id) + "\nJobtitle: "+ self.jobtitle + "\nJobdescription: " + self.jobdesc + "\nDeadline: " + str(self.deadline)

class PersonnelRequestSystem:
    def __init__(self):
        print("Initiating the Personnel Request System")
        self.requests = []
    def insert_request(self, personnelrequest):
        self.requests.append(personnelrequest)
    def print_all(self):
        if self.requests == []:
            print("No personnel requests avaialble")
        else:
            print("Printing all personnel requests")
            for request in self.requests:
                print(request)
                print("==========================")

system = PersonnelRequestSystem()