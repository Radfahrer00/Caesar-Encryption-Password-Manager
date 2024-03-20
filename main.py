from CipherAlphabet import CipherAlphabet
from CaesarCipher import CaesarCipher


def main_menu():
    """
    Displays the main menu and prompts the user for an action.

    Returns:
        str: The user's choice.
    """
    print("Main Menu:")
    print("1. Add a new password")
    print("2. See all encrypted passwords")
    print("3. Retrieve password for a service")
    print("4. Exit")
    choice = input("What do you want to do? Enter the number: ")
    return choice


def add_password(passwords, alphabet):
    """
    Adds a new password to the dictionary after encrypting it.

    Parameters:
        passwords (dict): A dictionary to store service names as keys and encrypted passwords as values.
        alphabet (CipherAlphabet): The alphabet used for encrypting the password.
    """
    service = input("Enter the service (e.g., 'email', 'social media'): ")
    password = input("Enter the password: ")

    encrypted_password = caesar_encryption(alphabet, password)
    passwords[service] = encrypted_password
    print("Password added successfully!")


def caesar_encryption(alphabet, password):
    """
    Encrypts a password using the Caesar cipher and asking the user for the key.

    Parameters:
        alphabet (CipherAlphabet): The alphabet used for the Caesar cipher encryption.
        password (str): The password to be encrypted.

    Returns:
        str: The encrypted password.
    """
    while True:
        key = input("Enter the encryption key. It should only be one character: ")
        if len(key) == 1:
            if alphabet.in_alphabet(key):
                break
            else:
                print("The encryption key is not in the defined alphabet. Choose another one.")
        else:
            print("Please enter only one character!")
    cipher = CaesarCipher(alphabet=alphabet)
    encrypted_password = cipher.encrypt(password, key) + key
    return encrypted_password


def see_all_passwords(passwords):
    """
    Displays all stored services and their corresponding encrypted passwords.

    Parameters:
        passwords (dict): The dictionary containing the services and their encrypted passwords.
    """
    if passwords:
        print("---------------Your passwords---------------")
        for service, password in passwords.items():
            print(f"Service: {service}, Password: {password}")
        print("--------------------------------------------")
    else:
        print("No passwords stored.")


def retrieve_password_for_service(passwords, alphabet):
    """
    Allows the user to select a service and decrypts the password for that service.

    Parameters:
        passwords (dict): The dictionary containing the services and their encrypted passwords.
        alphabet (CipherAlphabet): The alphabet used for decrypting the password.
    """
    if not passwords:
        print("No passwords stored.")
        return

    print("----------Services available----------")
    services = list(passwords.keys())
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")
    print("--------------------------------------")

    while True:
        try:
            choice = int(input("Enter the number for the service you want to retrieve the password for: "))
            if 1 <= choice <= len(services):
                selected_service = services[choice - 1]
                print(f"The encrypted password for {selected_service} is: {passwords[selected_service]}")
                key = passwords[selected_service][-1] # Last character is the key
                password_to_decrypt = passwords[selected_service][:-1] # Remove the key from the end
                cipher = CaesarCipher(alphabet=alphabet)
                decrypted_password = cipher.decrypt(password_to_decrypt, key)
                print(f"The decrypted password for {selected_service} is: {decrypted_password}")
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a number.")


def main():
    """
    The main function to run the password manager program.
    """
    alphabet = CipherAlphabet("0", "z")
    passwords = {}
    print("Welcome to the Classic Cryptography Password Manager!")
    while True:
        choice = main_menu()
        if choice == "1":
            add_password(passwords, alphabet)
        elif choice == "2":
            see_all_passwords(passwords)
        elif choice == "3":
            retrieve_password_for_service(passwords, alphabet)
        elif choice == "4":
            print("Exiting. Have a good day!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()