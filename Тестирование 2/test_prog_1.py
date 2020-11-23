import locale
from subprocess import Popen, PIPE, TimeoutExpired
import unittest

class TestCalcAcceptance(unittest.TestCase):
    ENCODING = locale.getpreferredencoding()
    PROCESS_WITH_ARGS = ('python3', 'prog_1.py')
    PROCESS_TIMEOUT = 5
    INPUT_SIGNATURE = 'Введіть Ваш рядок: '
    MESSAGE_SIGNATURE_EMPTY_STRING = 'Рядок не задовольняє умові. Рядок порожній.'
    MESSAGE_SIGNATURE_QUANTITY_SYM = 'Рядок не задовольняє умові. Число не дорівнює к-сті символів в рядку.'
    MESSAGE_SIGNATURE_NO_NUM = 'Рядок не задовольняє умові. У рядку немає чисел.'
    MESSAGE_SIGNATURE_MANY_NUM = 'Рядок не задовольняє умові. У рядку більше ніж одне число.'
    def run_subprocess(self, input_value):
        try:
            proc = Popen(self.PROCESS_WITH_ARGS, 
                         stdin=PIPE,
                         stdout=PIPE,
                         stderr=PIPE)
            out_value, err_value = proc.communicate(input_value.encode(self.ENCODING),
                                                    timeout=self.PROCESS_TIMEOUT)
        except TimeoutExpired:
            proc.kill()
            out_value, err_value = proc.communicate()
        return out_value.decode(self.ENCODING), err_value.decode(self.ENCODING)
    

    def test_normal_input(self):

        input_data = [
            ('flwee6', 'Рядок задовольняє умові.'),
            ('ffrtger8', 'Рядок задовольняє умові.'),
            ('dd dd dd9', 'Рядок задовольняє умові.'),
            ('ffa8 fff', 'Рядок задовольняє умові.'),
        ]
        for input_str, expect_str in input_data:  
            output_str, error_str = self.run_subprocess(input_str) 
            actual_result = output_str.strip().split(self.INPUT_SIGNATURE)[-1]
            self.assertEqual(actual_result, expect_str)

    def test_empty_space(self):
        input_str = '   '
        output_str, err_str = self.run_subprocess(input_str)
        self.assertIn(self.MESSAGE_SIGNATURE_NO_NUM, output_str)

    def test_empty_string(self):
        input_str = '\n'
        output_str, err_str = self.run_subprocess(input_str)
        self.assertIn(self.MESSAGE_SIGNATURE_EMPTY_STRING, output_str)

    def test_many_numbers(self):
        input_data = [
            ('flwe6 df4', 'Рядок не задовольняє умові. У рядку більше ніж одне число.'),
            ('fe1 ff2', 'Рядок не задовольняє умові. У рядку більше ніж одне число.'),
        ]
        for input_str, expect_str in input_data:  
            output_str, error_str = self.run_subprocess(input_str) 
            self.assertIn(self.MESSAGE_SIGNATURE_MANY_NUM, output_str)
    def test_quantity_sym(self):
        input_data = [
            ('flwe8', 'Рядок не задовольняє умові. Число не дорівнює к-сті символів в рядку.'),
            ('fe1wegwgweg', 'Рядок не задовольняє умові. Число не дорівнює к-сті символів в рядку.'),
        ]
        for input_str, expect_str in input_data:  
            output_str, error_str = self.run_subprocess(input_str) 
            self.assertIn(self.MESSAGE_SIGNATURE_QUANTITY_SYM, output_str)
    def test_no_number(self):
        input_data = [
            ('flwewefweg', 'Рядок не задовольняє умові. У рядку немає чисел.'),
            ('fffffffff', 'Рядок не задовольняє умові. У рядку немає чисел.'),
        ]
        for input_str, expect_str in input_data:  
            output_str, error_str = self.run_subprocess(input_str) 
            self.assertIn(self.MESSAGE_SIGNATURE_NO_NUM, output_str)

if __name__ == '__main__':
    unittest.main()
