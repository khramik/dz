while True:
    while True:
        number1=input("Введите первое число: ")
        if number1.isdigit()== False :
            print("Не правилный формат ввода. Повторите попытку")
        else:
            break
    while True:
        number2=input("Введите второе число: ")
        if number2.isdigit()==False :
            print("Не правильный формат ввода. Повторите попытку")
        else:
            break
    while True:
        number3=input("Введите действие: ")
        if number3=="+" or number3=="-" or number3=="*" or number3=="/" :
            break
        else:
            print("Не правильный формат ввода. Повторите попытку")
    number1=int(number1)
    number2=int(number2)
    if number3=="+":
        res=number1+number2
        print(res)
    elif number3=="-":
        res=number1-number2
        print(res)
    elif number3=="*":
        res=number1*number2
        print(res)
    elif number3=="/" and number2!=0:
        res=number1/number2
        print(res)
    else:
        print("На ноль делить нельзя")
    while True:
        quis=input("Продолжить да/нет: ")
        if quis=="да":
            answer=0
            break
        elif quis=="нет":
            answer=1
            break
        else:
            print("Выберите да или нет")
    if answer==0:
        None
    elif answer==1:
        break
