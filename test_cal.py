import unittest
import cal


class MyTestCal(unittest.TestCase):
    def test_add(self):
        #result = cal.add()
        self.assertEqual(cal.add(10, 5), 15)
        self.assertEqual(cal.add(0, 0), 0)
        self.assertNotEqual(cal.add(10, 5), -5)

    def test_sub(self):
        # result = cal.add()
        self.assertEqual(cal.sub(10, 5), 5)
        self.assertEqual(cal.sub(0, 0), 0)
        self.assertNotEqual(cal.sub(10, 5), -5)

    def test_mul(self):
        # result = cal.add()
        self.assertEqual(cal.mul(10, 5), 50)
        self.assertEqual(cal.mul(0, 0), 0)
        self.assertNotEqual(cal.mul(10, 5), -5)

    def test_div(self):
        # result = cal.add()
        self.assertEqual(cal.div(10, 5), 2)
        self.assertEqual(cal.div(1, 1), 1)
        self.assertNotEqual(cal.div(10, 5), -2.5)


if __name__ == '__main__':
    unittest.main()
