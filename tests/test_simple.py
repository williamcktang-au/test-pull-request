# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        password = "12345678 testpr 2"
        self.assertEqual(add_one(5), 6)


if __name__ == '__main__':
    unittest.main()
