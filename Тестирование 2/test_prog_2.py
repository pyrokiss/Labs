import locale
from subprocess import Popen, PIPE, TimeoutExpired
import unittest


class TestRideSideExchange(unittest.TestCase):
    ENCODING = locale.getpreferredencoding()
    PROCESS_WITH_ARGS = ('python3', 'prog_2.py')
    PROCESS_TIMEOUT = 5
    INPUT_SIGNATURE = 'P: N: Задавайте числа через Enter!'
    EXCEPTION_SIGNATURE = 'Введено некоректні дані.'
    MESSAGE = 'Ви ввели неправильне число.'

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
            ('3\n5\n1\n2\n3\n4\n5\n',  'У списку чисел, які більше та менше ніж P, однакова к-сть.'),
            ('1\n5\n1\n2\n3\n4\n5\n',  'У списку чисел, які більше ніж P, більше.'),
            ('5\n5\n1\n2\n3\n4\n5\n',  'У списку чисел, які менше ніж P, більше.'),
        ]
        
        for input_str, expect_str in input_data:
            output_str, error_str = self.run_subprocess(input_str)
            actual_result = output_str.strip().split(self.INPUT_SIGNATURE)[-1].strip()
            self.assertEqual(actual_result, expect_str)

    def test_bad_input_arg(self):
        bad_input_data = [
            '\n\n',
            '3\nf\n',
            ' \n \n',
            '\n2\n',
        ]

        for input_str in bad_input_data:
            output_str, error_str = self.run_subprocess(input_str)
            self.assertIn(self.EXCEPTION_SIGNATURE, output_str)
    def test_bad_input_numbers(self):
        bad_input_data = [
            '2\n5\n1\nf\n',
            '2\n5\na\n',
        ]

        for input_str in bad_input_data:
            output_str, error_str = self.run_subprocess(input_str)
            self.assertIn(self.MESSAGE, output_str)
if __name__ == '__main__':
    unittest.main()
