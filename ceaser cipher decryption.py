def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isupper():
            decrypted_message += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - key - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message
def main():
    encrypted_message = input("Enter the encrypted message: ")
    key = int(input("Enter the key (an integer): "))
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)
if __name__ == "__main__":
    main()