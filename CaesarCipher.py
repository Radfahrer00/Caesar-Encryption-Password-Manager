from CipherAlphabet import CipherAlphabet


class CaesarCipher:
    """
    A class for encrypting and decrypting text using a Caesar cipher approach.
    This implementation allows for a custom alphabet to be used in the encryption and decryption processes.
    """

    def __init__(self, alphabet=None):
        """
        Initializes the CaesarCipher instance.

        Parameters:
        alphabet (CipherAlphabet, optional): An instance of the CipherAlphabet class to define the alphabet used for
        encryption and decryption. If None, a default CipherAlphabet instance is used.
        """
        if alphabet is None:
            self.alphabet = CipherAlphabet()
        else:
            self.alphabet = alphabet

    def map_to_origin(self, c):
        """
        Maps a character to its numerical offset from the first letter of the cipher alphabet.

        Parameters:
            c (str): The character to be mapped.

        Returns:
            int: The numerical offset of the character from the first letter of the cipher alphabet.
        """
        return ord(c) - ord(self.alphabet.real_first_letter)

    def map_to_alphabet_range(self, i):
        """
        Maps a numerical offset back to a character within the cipher alphabet.

        Parameters:
            i (int): The numerical offset to be mapped back to a character.

        Returns:
            str: The character corresponding to the given offset within the cipher alphabet.
        """
        return chr(i + ord(self.alphabet.real_first_letter))

    def encrypt_transformation(self, clear_char, key_char):
        """
        Performs the encryption transformation on a single character.

        Parameters:
            clear_char (str): The plaintext character to encrypt.
            key_char (str): The character from the key used for encryption.

        Returns:
            str: The encrypted character.
        """
        # Calculate the sum of offsets of clear_char and key_char, then apply modulo operation to fit within alphabet
        # size.
        addition = self.map_to_origin(clear_char) + self.map_to_origin(key_char)
        mapped_ciphered_block = addition % self.alphabet.size_alphabet
        # Reverse the previous translation to obtain the cipheredBlock
        ciphered_block = self.map_to_alphabet_range(mapped_ciphered_block)
        return ciphered_block

    def decrypt_transformation(self, cipher_char, key_char):
        """
        Performs the decryption transformation on a single character.

        Parameters:
            cipher_char (str): The ciphertext character to decrypt.
            key_char (str): The character from the key used for decryption.

        Returns:
            str: The decrypted character.
        """
        # Calculate the difference of offsets of cipher_char and key_char, adjust for alphabet size, and apply modulo
        # operation.
        sub = self.map_to_origin(cipher_char) - self.map_to_origin(key_char)
        p_sub = sub + self.alphabet.size_alphabet
        mapped_ciphered_block = p_sub % self.alphabet.size_alphabet
        # Reverse the previous translation to obtain the cipheredBlock
        clear_block = self.map_to_alphabet_range(mapped_ciphered_block)
        return clear_block

    def encrypt(self, plain_text, key):
        """
        Encrypts an entire string of plaintext using a given key.

        Parameters:
            plain_text (str): The plaintext string to encrypt.
            key (str): The encryption key.

        Returns:
            str: The encrypted text.
        """
        cipher_text = []
        for plain_char in plain_text:
            if not self.alphabet.in_alphabet(plain_char):
                print("SKIPPING ONE CHARACTER.....")
                continue
            cipher_block = self.encrypt_transformation(plain_char, key)
            cipher_text.append(cipher_block)
        return ''.join(cipher_text)

    def decrypt(self, cipher_text, key):
        """
       Decrypts an entire string of ciphertext using a given key.

       Parameters:
           cipher_text (str): The ciphertext string to decrypt.
           key (str): The decryption key.

       Returns:
           str: The decrypted text.
       """
        plain_text = []
        for cipher_char in cipher_text:
            if not self.alphabet.in_alphabet(cipher_char):
                print("SKIPPING ONE CHARACTER.....")
                continue
            clear_block = self.decrypt_transformation(cipher_char, key)
            plain_text.append(clear_block)
        return ''.join(plain_text)
