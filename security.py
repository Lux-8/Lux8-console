users = {
    "artem":{"password": "123"}
}

def int_user_login():
  user_login = str(input("Введите логин: "))
  return user_login

def int_password(user):
  user_password = (input(f"Введите пароль для пользователя {user}: "))
  return user_password

def check_keys(user_password, login):
  if login in users:
    if user_password == users[login]["password"]:
      return True
    else:
      print("Неправильный пароль")
      return False
  else:
    print("Неправильный логин")
    return False