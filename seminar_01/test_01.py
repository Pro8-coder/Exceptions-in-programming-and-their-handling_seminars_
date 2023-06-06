from HW_01 import MyException
import unittest


class MyTest(unittest.TestCase):
    def test_handle_division(self):
        with self.assertRaises(ZeroDivisionError):
            MyException().handle_division()

    def test_handle_index_error(self):
        with self.assertRaises(IndexError):
            MyException().handle_index_error()

    def test_handle_key_error(self):
        with self.assertRaises(KeyError):
            MyException().handle_key_error()


if __name__ == '__main__':
    unittest.main()
