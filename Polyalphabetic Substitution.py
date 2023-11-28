def generate_vigenere_key(keyword, length):
    # Repeat the keyword to match the length of the text
    repeated_keyword = (keyword * (length // len(keyword))) + keyword[:length % len(keyword)]
    return repeated_keyword.upper()

def encrypt(plaintext, keyword):
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Preserve the case of the letter
            is_upper = plaintext[i].isupper()
            # Apply the Vigenère cipher shift
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            encrypted_char = chr((ord(plaintext[i].upper()) + shift - ord('A')) % 26 + ord('A'))
            ciphertext += encrypted_char.upper() if is_upper else encrypted_char.lower()
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, keyword):
    # To decrypt, we use the opposite shift
    reverse_shift = lambda char, shift: chr((ord(char.upper()) - shift - ord('A')) % 26 + ord('A'))

    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Preserve the case of the letter
            is_upper = ciphertext[i].isupper()
            # Apply the reverse Vigenère cipher shift
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            decrypted_char = reverse_shift(ciphertext[i], shift)
            plaintext += decrypted_char.upper() if is_upper else decrypted_char.lower()
        else:
            plaintext += ciphertext[i]
    return plaintext

def main():
    keyword = input("Enter the keyword: ").upper()
    plaintext = input("Enter the plaintext: ")

    keyword = generate_vigenere_key(keyword, len(plaintext))
    ciphertext = encrypt(plaintext, keyword)
    print(f"Encrypted text: {ciphertext}")

    decrypted_text = decrypt(ciphertext, keyword)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
