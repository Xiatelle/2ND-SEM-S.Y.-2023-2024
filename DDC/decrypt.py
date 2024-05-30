dict = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18,
    "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}


# Accept key from the user
key = int(input("Enter Key (1-25): "))
if key < 1 or key > 25:
    print("Invalid key. Key must be between 1 and 25.")
    exit()

# Accept message from the user
message = input("Enter the message: ")

decrypted_message = ""

# Encrypt the message
for char in message:
    if char.upper() in dict:
        decrypted_char_index = (dict[char.upper()] - key) % 26 #Additive Cypher Formula
        for letter, index in dict.items():
            if index == decrypted_char_index:
                decrypted_char = letter
                break
    else:
        decrypted_char = char
    decrypted_message += decrypted_char
print("=" * 25)
print("Decrypted message:", decrypted_message)
