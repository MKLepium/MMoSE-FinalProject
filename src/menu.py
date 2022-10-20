from src import event
from src import user_database
from src import personnelrequest
from src import financialrequest
def menu_display(User):
    menu_default()
    choice = int(input("What do you want to do: "))
    if choice == 0:
        return
    if choice == 1:
        event_viewer()
        menu_display(User)
        return
    if choice == 2:
        if User.role == user_database.Role.CustomerServiceSenior:
            customer_senior_screen(User)
        elif User.role == user_database.Role.CustomerServiceOfficer:
            customer_service_officer(User)
        elif User.role == user_database.Role.FinancialManager:
            financial_manager(User)
        elif User.role == user_database.Role.AdministrationManager:
            administration_manager(User)
        elif User.role == user_database.Role.ServiceManager:
            service_manager(User)
        elif User.role == user_database.Role.ServiceTeamMember:
            service_team_member(User)
        elif User.role == user_database.Role.HumanRessources:
            human_ressources(User)
        else:
            print("Please contact an Admin, Your Role is not recognised")
        menu_display(User)
        return
    else:
        print("Option not recognised.\nPlease Repeat")
        menu_display(User)
        return

def event_viewer():
    choice = int(input("0. Return\n1. View a specific Event\n2. View all Events\nWhat do you want to do: "))
    if choice == 0:
        return
    if choice == 1:
        event_id = int(input("Insert Event ID: "))
        specificed_event = event.event_system_3000.search_event(event_id)
        print(specificed_event)
    if choice == 2:
        event.event_system_3000.print_all()



def menu_default():
    print("0. Logout")
    print("1. Display Event(s)")
    print("2. View role dependent Options")

def customer_senior_screen(User):
    print("0. Initiate Event Request")
    print("1. Events requests awaiting approval")
    choice = int(input("Enter choice: "))
    if choice == 0:
        event.event_system_3000.insert_event(event.Event())
    elif choice == 1:
        event_approval()
    else:
        print("Option not recognised")

def event_approval():
    need_approval = list(filter( lambda x: x.status == "Wait For Approval", event.event_system_3000.events))
    if need_approval == []:
        print("No events need approval")
        return
    for specific_event in need_approval:
        check_approval(specific_event)

def check_approval(specific_event):
    print(specific_event)
    choice = input("Approve? [y/n]")
    if choice == "y":
        event.event_system_3000.search_event(specific_event.id).status = "Approval Given" # no none case since already found
    elif choice == "n":
        return #  continue to next
    else:
        print("Not recognized")
        check_approval(specific_event)

def customer_service_officer(User):
    print("0. Initiate Event Request")
    choice = input("What do you want to do: ")
    if choice == 0:
        event.event_system_3000.insert_event(event.Event())
    else:
        print("Option not recognised")


def financial_manager(User):
    print("0. View Financial Requests")
    print("1. Update Event Budget")
    choice = int(input("Enter choice: "))
    if choice == 0:
        financialrequest.system.print_all()
    if choice == 1:
        event_id = int(input("Insert Event ID: "))
        specificed_event = event.event_system_3000.search_event(event_id)
    else:
        print("Option not recognised")


def administration_manager(User):
    print("To be implemented")


def service_manager(User):
    print("0. Initiate Personnel Request")
    print("1. Initiate Financial Request")
    choice = int(input("Enter choice: "))
    if choice == 0:
        personnelrequest.system.insert_request(personnelrequest.PersonnelRequest())
    if choice == 1:
        financialrequest.system.insert_request(financialrequest.FinanicalRequest())
    else:
        print("Option not recognised")


def service_team_member(User):
    print("To be implemented")


def human_ressources(User):
    print("0. View Personnel Requests")
    choice = int(input("Enter choice: "))
    if choice == 0:
        personnelrequest.system.print_all()
    else:
        print("Option not recognised")


