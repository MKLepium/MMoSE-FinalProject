import user_database

def test_user_create():
   User = user_database.User("Johnny", "yeet", user_database.Role.AdministrationManager)
   assert User.name == "Johnny"
   assert User.password == "yeet"
   assert User.role == user_database.Role.AdministrationManager

def test_is_user_in_db():
   User = user_database.find_user('Johnny')
   assert User is not None