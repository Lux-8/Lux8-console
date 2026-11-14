import hashlib
import os

def make_hash(password: str) -> str:
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )
    return f"{salt.hex()}:{key.hex()}"


users = {
    "artem":{"password": make_hash("123")}
}


def int_user_login():
  user_login = str(input("Введите логин: "))
  return user_login

def int_password(user):
  user_password = (input(f"Введите пароль для пользователя {user}: "))
  return user_password

def check_keys(user_password, login):
  if login in users:
    stored = users[login]["password"]
    salt_hex, key_hex = stored.split(":")
    salt = bytes.fromhex(salt_hex)

    int_key = hashlib.pbkdf2_hmac(
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