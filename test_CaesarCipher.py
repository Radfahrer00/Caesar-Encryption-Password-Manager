import unittest
from CaesarCipher import CaesarCipher
from CipherAlphabet import CipherAlphabet


class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        self.alphabet = CipherAlphabet('a', 'z')
        self.cipher = CaesarCipher(self.alphabet)

    def test_encrypt_single_character(self):
        encrypted = self.cipher.encrypt('a', 'b')
        self.assertEqual(encrypted, 'b')

    def test_encrypt_single_character_2(self):
        encrypted = self.cipher.encrypt('b', 'e')
        self.assertEqual(encrypted, 'f')
        self.assertNotEqual(encrypted, 'e')
        self.assertNotEqual(encrypted, 'b')

    def test_decrypt_single_character(self):
        self.cipher = CaesarCipher(self.alphabet)
        decrypted = self.cipher.decrypt('b', 'b')
        self.assertEqual(decrypted, 'a')

    def test_decrypt_single_character_2(self):
        self.cipher = CaesarCipher(self.alphabet)
        decrypted = self.cipher.decrypt('f', 'e')
        self.assertEqual(decrypted, 'b')

    def test_encrypt_decrypt_word(self):
        phrase = "hello"
        key = "d"
        encrypted = self.cipher.encrypt(phrase, key)
        decrypted = self.cipher.decrypt(encrypted, key)
        self.assertEqual(decrypted, phrase)

    def test_encrypt_decrypt_word_2(self):
        phrase = "mynameisbob"
        key = "t"
        encrypted = self.cipher.encrypt(phrase, key)
        decrypted = self.cipher.decrypt(encrypted, key)
        self.assertEqual(decrypted, phrase)


if __name__ == '__main__':
    unittest.main()