import numpy as np
import matplotlib.pyplot as plt
import random
from tabulate import tabulate

def graph(array, name):
    title = plt.title(name)
    plot = plt.plot(array)
    plt.show()
    
def exp_dis(array):
    exp_value = np.mean(array)
    print("Мат. ожидание: ", round(exp_value, 5))
    dispersion = np.var(array)
    print("Дисперсия: ", round(dispersion, 5))
    print("")


#=======Поменять(Взято у Макса)=======#   
def get_interval(r_array, intervals):
    (element, counts) = np.unique(r_array, return_counts=True)
    result = []
    a = np.min(element) 
    step = (np.max(element) - np.min(element))/intervals
    b = a+step+0.0001
    n = 0
    for i in range(1, intervals + 1):
        count = counts[(a <= element) & (b >= element)]
        quantity = np.sum(count)
        n += quantity
        frequency = quantity/len(r_array)
        result.append((a, b, quantity, frequency))
        a = b
        b = b+step+0.0001
    return np.array(result)

def print_table(table_arr, table_header):
    table = [table_header]
    table_arr[2] = np.round(table_arr[2], 4)
    for i in table_arr:
        interval = "({}, {})".format(round(i[0], 2), round(i[1], 2))
        table.append([interval, int(i[2]), round(i[3], 4)])
    summa = "Сума: {}".format(int(np.sum(table_arr.T[2])))
    table.append(["", summa, ""])
    print(tabulate(table))

def get_dis_interval(r_array):
    (element, counts) = np.unique(r_array, return_counts=True)
    result = []
    for i, j in zip(element, counts):
        result.append([i, j, j / len(r_array)])
    return np.array(result)

def print_dis_table(table_arr, table_header):
    table = [table_header]
    table.extend(table_arr)
    summa = "Сума: {}".format(int(np.sum(table_arr.T[1])))
    table.append(["", summa, ""])
    print(tabulate(table))
#=======Поменять=======#

def histogramm(array, n, w, name):
    title = plt.title(name)
    plt.hist(array, n, rwidth=w, color='red')
    plt.show()

def monte_carlo(function, a, b, n):
    subsets = np.arange(0, n+1, n/10)
    steps = n/10
    u = np.zeros(n)
    for i in range(10):
        start = int(subsets[i])
        end = int(subsets[i+1])
        u[start:end] = np.random.uniform(low=i/10, high=(i+1)/10, size=end-start)
    np.random.shuffle(u)
    u_func = function(a+(b-a)*u)
    s = ((b-a)/n)*u_func.sum()
    return s
#===========================Завдання 1=====================================#
r_arr = np.random.rand(1000000)
head_arr = ["Інтервали", "Кількість", "Відносна частота"]
def task_1():
    graph(r_arr, "Завдання 1")
def task_1_1():
    exp_dis(r_arr)
def task_1_2():
    print_table(get_interval(r_arr, 10), head_arr)
def task_1_3():
    histogramm(r_arr, 10, 0.9, "Завдання 1.3")
def task_1_4():
    m = 1000
    a = 0
    max_arr = []
    while a<m:
        arr = np.random.rand(10000)
        mx = np.max(arr)
        max_arr.append(mx)
        a += 1
    histogramm(np.array(max_arr), 10, 0.9, "Завдання 1.4")
#===========================Завдання 2=====================================#
x = np.array([1, 10, 15, 23, 29, 38, 42])
p = np.array([0.02, 0.05, 0.1, 0.28, 0.23, 0.22, 0.1])
r_arr = np.random.choice(x, 1000, p=p)
def task_2():
    graph(r_arr, "Завдання 2")
def task_2_1():
    exp_dis(r_arr)
def task_2_2():
    print_dis_table(get_dis_interval(r_arr), head_arr)
def task_2_3():
    histogramm(r_arr, 10, 0.9, "Завдання 2")
#===========================Завдання 3=====================================#
def task_3_a1():
    a1 = np.random.rand(1000000)
    a2 = np.random.rand(1000000)
    formula = np.sqrt(-2*np.log(a1))*np.cos(2*np.pi*a2)
    histogramm(formula, 1000, 1, "Завдання 3")   
def task_3_a2():
    a1 = np.random.rand(1000000)
    a2 = np.random.rand(1000000)
    formula = np.sqrt(-2*np.log(a1))*np.sin(2*np.pi*a2)
    histogramm(formula, 1000, 1, "Завдання 3")
def task_3_b():
    n1, n2, n3 = 12, 48, 3
    formula1 = [np.sqrt(12/n1)*(np.sum(np.random.rand(n1))-0.5) for i in range(100000)]
    graf1=np.array(formula1)
    formula2 = [np.sqrt(12/n2)*(np.sum(np.random.rand(n2))-0.5) for i in range(100000)]
    graf2=np.array(formula2)
    formula3 = [np.sqrt(12/n3)*(np.sum(np.random.rand(n3))-0.5) for i in range(100000)]
    graf3=np.array(formula3)
    g1 = plt.hist(graf1, 100)
    g2 = plt.hist(graf2, 100)
    g3 = plt.hist(graf3, 100)
    plt.show()
#===========================Завдання 4=====================================#
wei_arr = np.random.weibull(5, 10000)
ray_arr = np.random.rayleigh(5, 10000)
lognorm_arr = np.random.lognormal(5, 1, 10000)
cauchy_arr = np.random.standard_cauchy(10000)
nak_arr = np.random.standard_gamma(5, 10000)
def task_4():
    graph(wei_arr, "Вейбулла")
    graph(ray_arr, "Релея")
    graph(lognorm_arr, "Логнормальний")
    graph(cauchy_arr, "Коші")
    graph(nak_arr, "Накагамі")
def task_4_1():
    print("Вейбулла:")
    exp_dis(wei_arr)
    print("Релея:")
    exp_dis(ray_arr)
    print("Логнормальний:")
    exp_dis(lognorm_arr)
    cauchy = np.array(cauchy_arr)
    print("Коші:")
    exp_dis(cauchy_arr)
    print("Накагамі:")
    exp_dis(nak_arr)
def task_4_2():
    print("Вейбулла:")
    print_table(get_interval(wei_arr, 10), head_arr)
    print("Релея:")
    print_table(get_interval(ray_arr, 10), head_arr)
    print("Логнормальний:")
    print_table(get_interval(lognorm_arr, 10), head_arr)
    print("Коші:")
    print_table(get_interval(cauchy_arr, 10), head_arr)
    print("Накагамі:")
    print_table(get_interval(nak_arr, 10), head_arr)
def task_4_3():
    histogramm(wei_arr, 10, 0.9, "Вейбулла")
    histogramm(ray_arr, 10, 0.9, "Релея")
    histogramm(lognorm_arr, 10, 0.9, "Логнормальний")
    histogramm(cauchy_arr, 10, 0.9, "Коші")
    histogramm(nak_arr, 10, 0.9, "Накагамі")
#===========================Завдання 5=====================================#
def function_1(x):
    return(x**7 + x**5 + x**3)
def function_2(x):
    return(2*np.sin(3*x))
def function_3(x):
    return(1/((x+1)*np.sqrt(x)))

def task_5():
    print("Інтеграл 1:")
    integral_1 = monte_carlo(function_1, 0, 1, 100)
    print(integral_1)
    print("\nІнтеграл 2:")
    integral_2 = monte_carlo(function_2, 0, np.pi, 100)
    print(integral_2)    
    print("\nІнтеграл 3:")
    integral_3 = monte_carlo(function_3, 0, 2000, 100)
    print(integral_3)

#===========================Завдання 6=====================================#
def task_6():
    n = 1001
    r_arr = np.random.rand(n)
    new_arr = []
    for i in range(n):
        if r_arr[i-1] < r_arr[i]:
            new_arr.append(1)
        elif r_arr[i-1] >= r_arr[i]:
            new_arr.append(0)
    #arr = new_arr.remove(new_arr[0])
    plt.hist(np.array(new_arr))
    plt.show()
#===========================Завдання 7=====================================#    
def task_7():
    m = 1000
    a = 0
    max_arr = []
    for i in range(m):
        arr = np.random.normal(0, 1, 1000)
        mx = np.max(arr)
        max_arr.append(mx)
    histogramm(np.array(max_arr), 100, 1, "Завдання 7")
#==================Интерфейс================#
print("""Група: КМ-81
Студент: Донченко Богдан
Номер роботи: 1""")
n = 0
while n != "0":
    choice = str(input("Оберіть номер завдання: "))
    if choice == "1":
        print("Завдання 1")
        task_1()
        task_1_1()
        task_1_2()
        task_1_3()
        task_1_4()
    elif choice == "2":
        print("Завдання 2")
        task_2()
        task_2_1()
        task_2_2()
        task_2_3()
    elif choice == "3":
        print("Завдання 3")
        task_3_a1()
        task_3_a2()
        task_3_b()
    elif choice == "4":
        print("Завдання 4")
        task_4()
        task_4_1()
        task_4_2()
        task_4_3()
    elif choice == "5":
        print("Завдання 5")
        task_5()
    elif choice == "6":
        print("Завдання 6")
        task_6()
    elif choice == "7":
        print("Завдання 7")
        task_7()
    else:
        print("Данного завдання не існує. Оберіть інше.")
    n = str(input("Якщо хочете продовжити введіть будь-яку клавішу. Для виходу введіть '0': "))

