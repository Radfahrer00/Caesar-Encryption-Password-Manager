class CipherAlphabet:
    """
    A class to define a custom range of characters (alphabet) for encryption and decryption operations.

    The class allows for the definition of any continuous range of characters based on their ASCII values,
    providing flexibility for encryption algorithms that may require non-standard alphabets.
    """

    # Constants defining the Alphabet by default
    first_letter = '0'
    last_letter = 'z'

    def __init__(self, f_letter=first_letter, l_letter=last_letter):
        """
       Initializes the CipherAlphabet instance with a specified range of characters.

       The range is determined by the f_letter and l_letter parameters, which represent the first and last
       characters of the desired alphabet, respectively. If the parameters are not provided, the default
       range ('0' to 'z') is used. If f_letter is greater than l_letter, their values are swapped to ensure
       a valid range.

       Parameters:
           f_letter (str, optional): The first letter of the custom alphabet. Defaults to '0'.
           l_letter (str, optional): The last letter of the custom alphabet. Defaults to 'z'.
       """
        if f_letter <= l_letter:
            self.real_first_letter = f_letter
            self.real_last_letter = l_letter
        else:
            self.real_first_letter = l_letter
            self.real_last_letter = f_letter

        # Calculate the size of the Alphabet
        self.size_alphabet = ord(self.real_last_letter) - ord(self.real_first_letter) + 1

    def in_alphabet(self, letter):
        """
        Checks if a given letter is within the defined alphabet range.

        Parameters:
            letter (str): The letter to check.

        Returns:
            bool: True if the letter is within the alphabet range, False otherwise.
        """
        return self.real_first_letter <= letter <= self.real_last_letter
