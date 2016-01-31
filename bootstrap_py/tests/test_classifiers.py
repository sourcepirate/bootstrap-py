# -*- coding: utf-8 -*-
"""bootstrap_py.tests.test_classifiers."""
import unittest
import requests_mock
from bootstrap_py.classifiers import Classifiers


class ClassifiersTests(unittest.TestCase):
    """bootstrap_py.classifiers.Classifiers tests."""

    def setUp(self):
        """Prepare test data."""
        with requests_mock.Mocker() as mock:
            with open('bootstrap_py/tests/data/classifiers.txt') as fobj:
                data = fobj.read()
            mock.get(Classifiers.url,
                     text=data,
                     status_code=200)
        self.data = Classifiers()

    def test_licenses(self):
        """respond dict licenses."""
        self.assertEqual(len(self.data.licenses().keys()), 49)
        self.assertEqual(len(self.data.licenses().values()), 49)
