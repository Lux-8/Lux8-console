import hashlib
import os

def make_hash(password: str) -> str: # делает хэш пароля с солью из списка и уже хранит захэшированный пароль
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )
    return f"{salt.hex()}:{key.hex()}"


users = { # Список пользователей и их пароли
    "root":{"password": make_hash("*")}
}


def int_user_login(): # функция ввода логина
  user_login = str(input("Введите логин: "))
  return user_login

def int_password(user): # функция ввода пароля
  user_password = (input(f"Введите пароль для пользователя {user}: "))
  return user_password

def check_keys(user_password, login): # функция проверки пароля и логина
  if login in users: 
    stored = users[login]["password"]
    salt_hex, key_hex = stored.split(":") # разделения соли от хэша
    salt = bytes.fromhex(salt_hex) 

    int_key = hashlib.pbkdf2_hmac( # хэширование введеного пароля
      "sha256",
      user_password.encode("utf-8"),
      salt,
      100_000
    )


    if int_key.hex() == key_hex: 
      return True
    else:
      print("Неправильный пароль")
      return False
  else:
    print("Неправильный логин")
    return False