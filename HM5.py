plus = int(input("Введите выручку фирмы "))
minus = int(input("Введите издержки фирмы "))
if plus > minus:
    print(f"Фирма работает с прибылью. Выручка составила {plus - minus}")
    rab = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль на одного сторудника сотавила {plus / rab}")
elif plus == minus:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
