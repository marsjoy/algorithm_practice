from unittest import TestCase
from challenges.hexadecimal import Hexadecimal
import logging


logger = logging.getLogger(__name__)


class TestHexadecimal(TestCase):
    def test_lookup_hexadecimal(self):
        self.assertEqual(Hexadecimal.lookup_hexadecimal(15), 'F')

    def test_convert_to_hexadecimal(self):
        self.assertEqual(Hexadecimal.convert_to_hexadecimal(254), 'EF')
        self.assertEqual(Hexadecimal.convert_to_hexadecimal(2504), '9C8')
        self.assertEqual(Hexadecimal.convert_to_hexadecimal(50), 23)
        self.assertEqual(Hexadecimal.convert_to_hexadecimal(2), 2)
        self.assertEqual(Hexadecimal.convert_to_hexadecimal(256), 100)

