import unittest
from core import concat_2_str

class TestCore(unittest.TestCase):
    def test_concat_2_str(self):
        test_cases = [
            (('hello', 'world'), 'hello world'),
            (('123', '456'), '123 456'),
            ((None, None), 'None None'),
        ]
        for inp, out in test_cases:
            self.assertEqual(concat_2_str(*inp), out)

if __name__ == '__main__':
    unittest.main()