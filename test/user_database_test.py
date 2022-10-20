import user_database

def test_user_create():
   User = user_database.User("Johnny", "yeet", user_database.Role.AdministrationManager)
   assert User.name == "Johnny"
   assert User.password == "yeet"
   assert User.role == user_database.Role.AdministrationManager

