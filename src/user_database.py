
from enum import Enum

class Role(Enum):
    CustomerServiceSenior = 1
    CustomerServiceOfficer = 2
    FinancialManager = 3
    AdministrationManager = 4
    ServiceManager = 5
    ServiceTeamMember = 6
    HumanRessources = 7


class User:
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role
    def __repr__(self):
        return "Name: " + self.name + "\nPassword: "+ self.password + "\nRole:" + str(self.role) + "\n\n"
    def __str__(self):
        return "Name: " + self.name + "\nPassword: "+ self.password + "\nRole:" + str(self.role) + "\n\n"

users = [
    User('Janet', 'asdf', Role.CustomerServiceSenior),
    User('Sarah', 'asdf', Role.CustomerServiceOfficer),
    User('Alice', 'asdf', Role.FinancialManager),
    User('Mike', 'asdf', Role.AdministrationManager),
    User('Natalie', 'asdf', Role.ServiceManager),
    User('Johnny', 'asdf', Role.ServiceTeamMember),
    User('Simon', 'asdf', Role.HumanRessources),
]
