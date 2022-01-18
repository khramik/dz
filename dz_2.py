

given_string= '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
given_string=given_string.strip()
print(given_string)
print(given_string.count("a"))
print(given_string.upper())
print(given_string.lower())
print(given_string.replace("super power", "tasty breakfast"))
print(given_string.isalpha())
given_string=given_string.replace(" ", "-")
given_string=given_string.replace("i", "1")
print(given_string)


name=input("Введите имя: ")
surname=input(name + " " + "Введите фамилию: ")
patronymic=input(surname + " " + name + " " +"Введите отчество: ")
birthday=input(surname + " " + name + " " + patronymic + " " + "Введите дату рождения (Пример:01.01.2022): ")
FIO=surname[0]+name[0]+patronymic[0]
print("ФИО:",FIO)
print("Фамилия:",surname)
print("Имя:",name)
print("Отчество:",patronymic)
print("Дата рождения:",birthday)
