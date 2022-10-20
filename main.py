"""
    Startup and welcoming of the user.
"""
from src import login

def main():
    User = login.start()
    print(User)

if __name__ == "__main__":
    main()

