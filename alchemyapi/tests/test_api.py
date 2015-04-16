from __future__ import print_function

import sys
import os
import nose

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from ..api import AlchemyAPI

__all__ = ['TestAPI']


class TestAPI(unittest.TestCase):

    def test_endpoints(self):
        pass


if __name__ == '__main__':
    nose.main()
