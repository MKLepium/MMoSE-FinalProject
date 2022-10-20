import itertools

class FinancialRequest:
    newid = itertools.count()
        
    def __init__(self):
        self.event = input("Which event is this finanical request associated with: ")
        self.money = input("How much budget would you like to request: ")
        self.reason = input("Please provide a short reason for this financial request: ")
        self.id = next(FinancialRequest().newid)
    def __repr__(self):
        return "Id: " + str(self.id) + "\nAssociated Event: "+ self.event + "\nRequested Budget: " + self.money + "\nReason: " + self.reason
    def __str__(self):
        return "Id: " + str(self.id) + "\nAssociated Event: "+ self.event + "\nRequested Budget: " + self.money + "\nReason: " + self.reason

class FinancialRequestSystem:
    def __init__(self):
        print("Initiating the Financial Request System")
        self.requests = []
        # self.events = [Event(_Debug=True), Event(_Debug=True), Event(_Debug=True)]
    # def search_event(self, id):
    #     return next((x for x in self.events if x.id == name), None)
    def insert_request(self, financialrequest):
        self.requests.append(financialrequest)
    def print_all(self):
        if self.requests == []:
            print("No financial requests avaialble")
        else:
            print("Printing all financial requests")
            for request in self.requests:
                print(request)
                print("==========================")

system = FinancialRequestSystem()