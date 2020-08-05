import unittest
import capital


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = 'python'
        result = capital.to_capial(text)
        self.assertEqual(result, 'PYTHON')


if __name__ == '__main__':
    unittest.main()
