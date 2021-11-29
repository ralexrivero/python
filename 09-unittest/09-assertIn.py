#!/usr/bin/env python3
import unittest

class test_assert(unittest.TestCase):

    def test_assertin(self):
        a = "Hello"
        b = "Hello World"
        self.assertIn(a, b, "Not include")

""" if __name__ == "__main__":
    unittest.main() """
