import re
def task_2(p, n):
    arr = []
    p = float(p)
    n = float(n)
    n = int(n)
    print("Задавайте числа через Enter!")
    while len(arr) < n:
        elem = input("")
        res = re.match(r'-\d|\d', elem)
        if res == None:
            return "Ви ввели неправильне число."
        else:
            arr.append(float(elem))

    new_list = sorted(arr)
    b_p = 0
    l_p = 0
    for i in new_list:
        if i > p:
            b_p += 1
        elif i < p:
            l_p += 1
    if b_p > l_p:
        return "У списку чисел, які більше ніж P, більше."
    elif b_p < l_p:
        return "У списку чисел, які менше ніж P, більше."
    elif b_p == l_p:
        return "У списку чисел, які більше та менше ніж P, однакова к-сть."

if __name__ == "__main__":
    p = input("P: ")
    res1 = re.match(r'-\d|\d', p)
    n = input("N: ")
    res2 = re.match(r'\d|\d.0', n)
    if res1 == None or res2 == None:
        print("Введено некоректні дані.")
    else:
        print(task_2(p, n))

    
