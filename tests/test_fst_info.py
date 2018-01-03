import unittest

from core.fst_info import FstInfo

class TestFstInfo(unittest.TestCase):
    def test_get_info(self):
        expected_bytes = 'some_text'.encode()

        fst_info = FstInfo('cat')
        output = fst_info.get_info(expected_bytes)
        self.assertEqual(output, expected_bytes)


if __name__ == '__main__':
    unittest.main()
