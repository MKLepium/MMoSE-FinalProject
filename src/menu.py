from src import event
from src import user_database
from src import personnelrequest
from src import financialrequest
from src import task
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
        event.event_system_3000.insert_event(event.Event(task.system))
    elif choice == 1:
        initial_event_approval()
    else:
        print("Option not recognised")

def initial_event_approval():
    need_approval = event.event_system_3000.by_status("Wait For Approval")
    if need_approval == []:
        print("No events need approval")
        return
    for specific_event in need_approval:
        specific_event.first_approval()

def customer_service_officer(User):
    print("0. Initiate Event Request")
    choice = input("What do you want to do: ")
    if choice == 0:
        event.event_system_3000.insert_event(event.Event(task.system))
    else:
        print("Option not recognised")


def financial_manager(User):
    print("0. View Financial Requests")
    print("1. Update Event Budget")
    print("2: Event requests awaiting financial review")
    choice = int(input("Enter choice: "))
    if choice == 0:
        financialrequest.system.print_all()
    elif choice == 1:
        event_id = int(input("Insert Event ID: "))
        specificed_event = event.event_system_3000.search_event(event_id)
        if specificed_event == None:
            print("No event found.")
            return
        else:
            specificed_event.budget.update()
            print("Event saved:")
            print(specificed_event)
            print("==========================")
    elif choice == 2:
        finanical_event_approval()
    else:
        print("Option not recognised")

def finanical_event_approval():
    need_approval = event.event_system_3000.by_status("In Financial Review")
    if need_approval == []:
        print("No events need approval")
        return
    for specific_event in need_approval:
        specific_event.financial_approval()


def administration_manager(User):
    print("0: Event requests awaiting final review")
    choice = int(input("What do you want to do: "))
    if choice == 0:
        need_approval = event.event_system_3000.by_status("In Final Review")
        if need_approval == []:
            print("No events need approval")
            return
        for specific_event in need_approval:
            specific_event.final_approval()
    else:
        print("Option not recognised")


def service_manager(User):
    print("0. Initiate Personnel Request")
    print("1. Initiate Financial Request")
    print("2. Add task for an event")
    print("3. See task list")
    print("4. Close task")
    choice = int(input("Enter choice: "))
    if choice == 0:
        personnelrequest.system.insert_request(personnelrequest.PersonnelRequest())
    elif choice == 1:
        financialrequest.system.insert_request(financialrequest.FinancialRequest())
    elif choice == 2:
        event_id = int(input("Insert Event ID: "))
        specificed_event = event.event_system_3000.search_event(event_id)
        if specificed_event == None:
            print("No event found.")
            return
        else:
            task.system.insert_task(task.Task(specificed_event))
            print("==========================")
            print(f"All task list for {specificed_event.name}:")
            print("- " + '\n- '.join(map(str, specificed_event.tasks())))
            print("==========================")
    elif choice == 3:
        task.system.print_all()
    elif choice == 4:
        task_id = int(input("Insert Task ID: "))
        specificed_task = task.system.search_task(task_id)
        if specificed_task == None:
            print("No task found.")
            return
        else:
            specificed_task.close()
    else:
        print("Option not recognised")


def service_team_member(User):
    print("0. See task list")
    choice = int(input("Enter choice: "))
    if choice == 0:
        task.system.print_all()
    else:
        print("Option not recognised")


def human_ressources(User):
    print("0. View Personnel Requests")
    choice = int(input("Enter choice: "))
    if choice == 0:
        personnelrequest.system.print_all()
    else:
        print("Option not recognised")


