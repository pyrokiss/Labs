import math
print("Варіант 28")
def rad_to_grad(x):
    res = math.degrees(x)
    return round(res, 2)
def grad_to_rad(x):
    res = math.radians(x)
    return round(res, 2)
choice = str(input("""
1) Перевод из радиан в градусы;
2) Перевод из градусов в радианы.
Ваш выбор: """))
if choice == "1":
    radian = float(input("Введите радианы: "))
    result = rad_to_grad(radian)
    print(result)
elif choice == '2':
    degrees = float(input("Введите градусы: "))
    result = grad_to_rad(degrees)
    print(result)
else:
    print("Данной операции нету!")
