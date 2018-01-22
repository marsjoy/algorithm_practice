from unittest import TestCase
from challenges import hexadecimal
import logging


logger = logging.getLogger(__name__)


class TestHexadecimal(TestCase):

    def test_convert_to_hexadecimal(self):
        self.assertEqual(hexadecimal.convert_to_hexadecimal(254), 'FE')
        self.assertEqual(hexadecimal.convert_to_hexadecimal(2504), '9C8')
        self.assertEqual(hexadecimal.convert_to_hexadecimal(50), '32')
        self.assertEqual(hexadecimal.convert_to_hexadecimal(2), '2')
        self.assertEqual(hexadecimal.convert_to_hexadecimal(256), '100')

    def test_convert_to_hexadecimal_recursive(self):
        self.assertEqual(hexadecimal.convert_to_hexadecimal_recursive(254), 'FE')
        self.assertEqual(hexadecimal.convert_to_hexadecimal_recursive(2504), '9C8')
        self.assertEqual(hexadecimal.convert_to_hexadecimal_recursive(50), '32')
        self.assertEqual(hexadecimal.convert_to_hexadecimal_recursive(2), '2')
        self.assertEqual(hexadecimal.convert_to_hexadecimal_recursive(256), '100')

