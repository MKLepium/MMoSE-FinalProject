
import itertools
from datetime import date


class Event:
    newid = itertools.count()
        
    def __init__(self):
        self.date = input("What is the date of the Event: ")
        self.name = input("What is the name of the Event: ")
        self.active = False
        self.status = "Wait For Approval"
        """
        Wait For Approval
        Approval Given
        """
        self.expected_attendees = input("How many people are expected: ")
        self.tasks = []
        self.preferences = input("Additional Preferences: ")
        self.budget = Budget(self)
        self.id = next(Event.newid)
    def __repr__(self):
        return "Name: " + self.name + "\nDate: "+ self.date + "\nId: " + str(self.id) + "\nBudget: " + str(self.budget.budget)
    def __str__(self):
        return "Name: " + self.name + "\nDate: "+ self.date + "\nId: " + str(self.id) + "\nBudget: " + str(self.budget.budget)

class Budget:
    def __init__(self, Event):
        self.event = Event
        self.budget = input("Expected Budget: ")

    def update(self):
        print(f"Current budget for event {self.event} is  {self.budget}.")
        new_budget = input("What should the new budget be: ")
        choice = input(f"Do you want to safe {new_budget} as the new budget? [y/n]")
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
    def print_all(self):
        if self.events == []:
            print("No Events avaialble")
        else:
            print("Printing all Events")
            for event in self.events:
                print(event)
                print("==========================")
    
    
event_system_3000 = EventSystem()