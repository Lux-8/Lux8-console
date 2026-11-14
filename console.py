def console(login, access): #Проверяет разрешение и если разрешено впускает в коносль
  if access:
    print(f"Добро пожаловать в консоль")
  else:
    print("///error///")