def read_phone_numbers():
    """
    Collects names and phone numbers from the user to build a phonebook.
    Returns:
        dict: A dictionary containing names as keys and numbers as values.
    """
    phonebook = {}
    print("Enter names and numbers. Leave the name blank to stop.")
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        number = input("Number: ").strip()
        phonebook[name] = number
    return phonebook


def print_phonebook(phonebook):
    """
    Prints all the names and numbers in the phonebook.
    Args:
        phonebook (dict): The phonebook dictionary.
    """
    print("\nPhonebook entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows the user to look up numbers in the phonebook by entering a name.
    Args:
        phonebook (dict): The phonebook dictionary.
    """
    print("\nLookup phone numbers. Leave the name blank to stop.")
    while True:
        name = input("Enter name to lookup: ").strip()
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    """
    Main function to manage the phonebook:
    - Reads phonebook entries
    - Displays the phonebook
    - Allows user to look up numbers
    """
    print("Welcome to the Phonebook Program!")
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
