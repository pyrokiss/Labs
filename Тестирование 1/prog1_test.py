import unittest
from prog1 import rad_to_grad, grad_to_rad

class Lab1Test(unittest.TestCase):
        #Проверка на 1
    def test_rad_to_grad_correct1(self):
        self.assertEqual(rad_to_grad(1), 57.3)
        #Проверка на 2
    def test_rad_to_grad_correct2(self):
        self.assertEqual(rad_to_grad(2), 114.59)
        #Проверка на "s"
    def test_rad_to_grad_error1(self):
        self.assertRaises(TypeError, rad_to_grad, "s")
        #Проверка на "testing"
    def test_rad_to_grad_error2(self):
        self.assertRaises(TypeError, rad_to_grad, "testing")
        #Проверка на ""
    def test_rad_to_grad_empty(self):
        self.assertRaises(TypeError, rad_to_grad, "")

        #Проверка на 30
    def test_grad_to_rad_correct1(self):
        self.assertEqual(grad_to_rad(30), 0.52)
        #Проверка на 90
    def test_grad_to_rad_correct2(self):
        self.assertEqual(grad_to_rad(90), 1.57)
        #Проверка на "v"
    def test_grad_to_rad_error1(self):
        self.assertRaises(TypeError, grad_to_rad, "v")
        #Проверка на "auto"
    def test_grad_to_rad_error2(self):
        self.assertRaises(TypeError, grad_to_rad, "auto")
        #Проверка на ""
    def test_grad_to_rad_empty(self):
        self.assertRaises(TypeError, grad_to_rad, "")
if __name__ == '__main__':
    unittest.main()
