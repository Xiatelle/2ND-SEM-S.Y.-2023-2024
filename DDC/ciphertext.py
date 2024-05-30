dict = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18,
    "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}

process = True

while process:

    option = input("Decrypt(D) or Encrypt(E): ")
    key = int(input("Enter Key (1-25): "))

    if option == "D":

        if key < 1 or key > 25:
            print("Invalid key. Key must be between 1 and 25.")
            exit()

        message = input("Enter the message: ")

        decrypted_message = ""


        for char in message:
            if char.upper() in dict:
                decrypted_char_index = (dict[char.upper()] - key) % 26
                for letter, index in dict.items():
                    if index == decrypted_char_index:
                        decrypted_char = letter
                        break
            else:
                decrypted_char = char
            decrypted_message += decrypted_char
        print("=" * 25)
        print("Decrypted message:", decrypted_message)

        continue_ = input("Continue? (Y/N): ")
        if continue_ == "Y":
            process = True
            print("=" * 25)
        else:
            process = False
            print("=" * 25)

    else:
        if key < 1 or key > 25:
            print("Invalid key. Key must be between 1 and 25.")
            exit()

        message = input("Enter the message: ")

        encrypted_message = ""

        for char in message:
            if char.upper() in dict:
                encrypted_char_index = (dict[char.upper()] + key) % 26
                for letter, index in dict.items():
                    if index == encrypted_char_index:
                        encrypted_char = letter
                        break
            else:
                encrypted_char = char
            encrypted_message += encrypted_char
        print("=" * 25)
        print("Encrypted message:", encrypted_message)

        continue_ = input("Continue? (Y/N): ")

        if continue_ == "Y":
            process = True
            print("=" * 25)
        else:
            process = False
            print("=" * 25)
