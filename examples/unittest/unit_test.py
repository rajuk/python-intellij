import unittest

class ExampleTest(unittest.TestCase):
    def test_foo(self):
        condition = True
        self.assertTrue(condition)

if __name__ == "__main__":
    unittest.main()