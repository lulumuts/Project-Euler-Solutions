import unittest

import smallest

class TestSmallest(unittest.TestCase):


    def tearDown(self):
        smallest.start_point = 1


    def test_range_generator(self):

        input = 20
        range_length=len(smallest.range_generator(input))
        self.assertTrue(range_length==20)


    def test_start_point_exists(self):
        start= smallest.start_point
        self.assertEqual(1,start)

    def test_start_point_increment(self):

        smallest.increment_start()
        start= smallest.start_point
        self.assertEqual(start,2)

    def test_check_divisibility_false(self):


        divisible=smallest.is_divisible(10,3)
        self.assertFalse(divisible)


    def test_check_divisibility_true(self):


        divisible=smallest.is_divisible(10,5)
        self.assertTrue(divisible)




if __name__ =="__main__":
    unittest.main()
