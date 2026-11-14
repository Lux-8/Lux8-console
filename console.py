commands = {
  "quit","new_user","set_pass"
}

def print_menu():
  print(f"Lux-8 console\ncommands: {commands}")

def console(login, access): #Проверяет разрешение и если разрешено впускает в коносль
  if access:
    print(f"Добро пожаловать в консоль")
    key = input("Введите \"*\" чтобы продолжить: ")
    if key == "*":
      print_menu()
  else:
    print("///error///")