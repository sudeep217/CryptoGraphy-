def decrypt_caesar(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - key - base) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text
def brute_force_caesar(ciphertext):
    for key in range(26):
        decrypted_text = decrypt_caesar(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")
def main():
    ciphertext = input("Enter the ciphertext: ")
    brute_force_caesar(ciphertext)
if __name__ == "__main__":
    main()