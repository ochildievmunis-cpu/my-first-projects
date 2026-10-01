contacts = {}
while True:
    print("Что хочешь сделать?")
    print("1 - Добавить контакт")
    print("2 - Показать все контакты")
    print("3 - Выход")
    choice = input("Твой выбор: ")
    if choice == "1":
       name = input("Имя: ")
       phone = input("Номер: ")
       contacts[name] = phone
       print("Контакт добавлен!")
    elif choice == "2":
        for name in contacts:
            print(name, "-", contacts[name])
    elif choice == "3":
        print("Пока!")
        break
    else:
        print("Неизвестный выбор!")
