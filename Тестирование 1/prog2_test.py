import unittest
from prog2 import list_task

class Lab1Test(unittest.TestCase):
    #Проверка на обычный список
    def test_task2_correct1(self):
        arr = [1, 5, 3, 7, 9]
        self.assertAlmostEqual(list_task(arr), 5.0)
    #Проверка на список с числами с плавующей точкой
    def test_task2_correct2(self):
        arr = [1.6, 5.2, 3.2, 7.5, 9.4]
        self.assertAlmostEqual(list_task(arr), 5.38)
    #Проверка на минусовые числа
    def test_task2_correct3(self):
        arr = [-1, -5, -8, -6, -9]
        self.assertAlmostEqual(list_task(arr), -5.8)
    #Проверка на другие типы данных
    def test_task2_string(self):
        arr = [1, 5, "3", 7, 9]
        self.assertRaises(TypeError, list_task, arr)
    #Проверка на пустой список
    def test_task2_empty(self):
        arr = []
        self.assertRaises(ZeroDivisionError, list_task, arr)



if __name__ == "__main__":
    unittest.main()
