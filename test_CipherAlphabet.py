import unittest
from CipherAlphabet import CipherAlphabet


class TestCipherAlphabet(unittest.TestCase):

    def test_alphabet_range(self):
        alphabet = CipherAlphabet('a', 'f')
        self.assertEqual(alphabet.real_first_letter, 'a')
        self.assertEqual(alphabet.real_last_letter, 'f')
        self.assertEqual(alphabet.size_alphabet, 6)

    def test_alphabet_range_2(self):
        alphabet = CipherAlphabet('0', 'Z')
        self.assertEqual(alphabet.real_first_letter, '0')
        self.assertEqual(alphabet.real_last_letter, 'Z')
        self.assertEqual(alphabet.size_alphabet, 43)

    def test_alphabet_range_3(self):
        alphabet = CipherAlphabet('0', 'd')
        self.assertEqual(alphabet.real_first_letter, '0')
        self.assertEqual(alphabet.real_last_letter, 'd')
        self.assertEqual(alphabet.size_alphabet, 53)
        self.assertNotEqual(alphabet.size_alphabet, 40)

    def test_in_alphabet(self):
        alphabet = CipherAlphabet('a', 'f')
        self.assertTrue(alphabet.in_alphabet('a'))
        self.assertTrue(alphabet.in_alphabet('c'))
        self.assertFalse(alphabet.in_alphabet('z'))

    def test_in_alphabet_2(self):
        alphabet = CipherAlphabet('A', 'f')
        self.assertTrue(alphabet.in_alphabet('D'))
        self.assertTrue(alphabet.in_alphabet('d'))
        self.assertFalse(alphabet.in_alphabet('g'))

    def test_in_alphabet_3(self):
        alphabet = CipherAlphabet('2', 'f')
        self.assertTrue(alphabet.in_alphabet('D'))
        self.assertTrue(alphabet.in_alphabet('6'))
        self.assertFalse(alphabet.in_alphabet('1'))

    def test_in_alphabet_4(self):
        alphabet = CipherAlphabet(' ', 'z')
        self.assertTrue(alphabet.in_alphabet('/'))
        self.assertTrue(alphabet.in_alphabet('('))
        self.assertTrue(alphabet.in_alphabet('R'))
        self.assertTrue(alphabet.in_alphabet('9'))
        self.assertTrue(alphabet.in_alphabet('='))
        self.assertTrue(alphabet.in_alphabet('_'))


if __name__ == '__main__':
    unittest.main()