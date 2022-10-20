def menu_display(User):
    if User.role == Role.CustomerServiceSenior:
        customer_senior_screen(User)
    if User.role == Role.CustomerServiceOfficer:
        customer_service_officer(User)
    if User.role == Role.FinancialManager:
        financial_manager(User)
    if User.role == Role.AdministrationManager:
        administration_manager(User)
    if User.role == Role.ServiceManager:
        service_manager(User)
    if User.role == Role.ServiceTeamMember:
        service_team_member(User)
    if User.role == Role.HumanRessources:
        human_ressources(User)

def customer_senior_screen():
    pass

def customer_service_officer():
    pass

def financial_manager():
    pass

def administration_manager():
    pass

def service_manager():
    pass

def service_team_member():
    pass

def human_ressources():
    pass

