def task_1(string):
    num_list = []
    num=''
    for i in string:
        if i.isdigit():
            num = num + i
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    if len(string) == 0:
        return "Рядок не задовольняє умові. Рядок порожній."
    if len(num_list) == 1:
        if num_list[0] == len(a):
            return "Рядок задовольняє умові."
        else:
            return "Рядок не задовольняє умові. Число не дорівнює к-сті символів в рядку."
    elif len(num_list) == 0:
        return "Рядок не задовольняє умові. У рядку немає чисел."
    else:
        return "Рядок не задовольняє умові. У рядку більше ніж одне число."
if __name__ == '__main__':
    a = str(input("Введіть Ваш рядок: "))
    print(task_1(a))
