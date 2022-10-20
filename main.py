"""
    Startup and welcoming of the user.
"""
from src import login
from src.user_database import Role
from src import display


def main():
    User = login.login()
    display.menu_display(User)

if __name__ == "__main__":
    main()

