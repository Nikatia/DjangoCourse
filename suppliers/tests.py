from django.test import TestCase
import unittest

from suppliers.laskin import plus, plus_complicated

# name of the test HAS TO start with "test"

class LaskinTests(TestCase):
    def test_plus(self):
        #tests, that numbers are added
        self.assertEqual(plus(7, 2), 9)
        self.assertEqual(plus(7.2, 3.7), 10.9)

    def test_plus_complicated(self):
        #testing adding with conditional if clause
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 8), 8)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 2), 19)
        self.assertEqual(plus('7', 2), 9)
