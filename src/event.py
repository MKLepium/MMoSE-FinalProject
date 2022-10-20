
import itertools

class Event:
    newid = itertools.count()
        
    def __init__(self, TaskSystem):
        self.__task_system = TaskSystem
        self.name = input("What is the name of the Event: ")
        self.date = input("What is the date of the Event: ")
        self.active = False
        self.status = "Wait For Approval"
        """
        Wait For Approval
        In Financial Review
        In Final Review
        Approved
        """
        self.expected_attendees = input("How many people are expected: ")
        self.tasks = self.get_tasks
        self.preferences = input("Additional Preferences: ")
        self.budget = Budget(self)
        self.financial_review = "pending"
        self.id = next(Event.newid)
    def get_tasks(self):
        return self.__task_system.by_event(self)
    def first_approval(self):
        print(self)
        choice = input(f"Approve event {self.id}? [y/n] ")
        if choice == "y":
            self.status = "In Financial Review"
        elif choice == "n":
            return #  continue to next
        else:
            print("Not recognized")
            self.first_approval()
    def financial_approval(self):
        print(self)
        choice = input(f"Approve event {self.id}? [y/n] ")
        if choice == "y":
            self.financial_review = input("Add your financial review: ")
            self.status = "In Final Review"
        elif choice == "n":
            return #  continue to next
        else:
            print("Not recognized")
            self.financial_approval()
    def final_approval(self):
        print(self)
        choice = input(f"Approve event {self.id}? [y/n] ")
        if choice == "y":
            self.status = "Approved"
        elif choice == "n":
            self.status = "Rejected"
        else:
            print("Not recognized")
            self.final_approval()
    def __repr__(self):
        return "Id: " + str(self.id) + "\nName: "+ self.name + "\nDate: " + self.date + "\nBudget: " + str(self.budget.budget) + "\nStatus: " + self.status + "\nFinancial Review: " + self.financial_review + "\nTasks: \n- " + '\n- '.join(map(str, self.tasks()))
    def __str__(self):
        return "Id: " + str(self.id) + "\nName: "+ self.name + "\nDate: " + self.date + "\nBudget: " + str(self.budget.budget) + "\nStatus: " + self.status + "\nFinancial Review: " + self.financial_review + "\nTasks: \n- " + '\n- '.join(map(str, self.tasks()))

class Budget:
    def __init__(self, Event):
        self.event = Event
        self.budget = input("Expected Budget: ")

    def update(self):
        print(f"Current budget for event {self.event.name} is {self.budget}.")
        new_budget = input("What should the new budget be: ")
        choice = input(f"Do you want to safe {new_budget} as the new budget? [y/n] ")
        if choice == "y":
            self.budget = new_budget
        else:
            self.update()

class EventSystem:
    def __init__(self):
        print("Initiating the Event System 3000")
        self.events = []
        # self.events = [Event(_Debug=True), Event(_Debug=True), Event(_Debug=True)]
    def search_event(self, id):
        for event in self.events:
            if event.id == id:
                return event
            else: 
                continue
        return None
    def insert_event(self, event):
        self.events.append(event)
    def by_status(self, status):
        return list(filter( lambda x: x.status == status, self.events))
    def print_all(self):
        if self.events == []:
            print("No Events avaialble")
        else:
            print("==========================")
            for event in self.events:
                print(event)
                print("==========================")
    
    
event_system_3000 = EventSystem()