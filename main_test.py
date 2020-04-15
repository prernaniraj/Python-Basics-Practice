import unittest
import main1 

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num  = 10
        result = main1.do_stuff(num)
        self.assertEqual(result, 15)
    def test_do_stuff1(self):
        num = "asdfas"
        result = main1.do_stuff(num)
        self.assertEqual(result, "Please enter number")


if __name__ == "__main__":
    unittest.main()