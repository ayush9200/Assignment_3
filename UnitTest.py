import unittest

import GraphDistance


class TestGraphDistance(unittest.TestCase):

    def run_test_cases(self):
        graph_distance = GraphDistance.GraphDistance()
        val = graph_distance.calculate_age(1995, 2021)
        self.assertEqual(val, 26)
        self.assertNotEqual(val, 23)

        val = graph_distance.calculate_stmt(101)
        self.assertTrue(val, True)
        val = graph_distance.calculate_stmt(89)
        self.assertFalse(val, False)

        s = 'Ayush Singh'
        self.assertEqual(s.split(), ['Ayush', 'Singh'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

        self.assertGreater(200, 52)
        self.assertLess(33, 40)

