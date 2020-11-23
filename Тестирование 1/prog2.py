print("Варінт 28")
def list_task(array):
    res = sum(array)/len(array)
    return res

N = int(input("Количество элементов в списке: "))
arr = []
for i in range(N):
    number = float(input("Введите число: "))
    arr.append(number)
print(list_task(arr))
