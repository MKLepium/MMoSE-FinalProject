"""
    Startup and welcoming of the user.
"""
from src import login
from src.user_database import Role
from src import menu
from src import event

def main():
    User = login.login()
    menu.menu_display(User)
    main()

if __name__ == "__main__":
    # Setup

    # Start
    main()

