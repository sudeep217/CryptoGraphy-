def generate_cipher_key():
    # This function generates a random monoalphabetic substitution key
    import random
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def encrypt(plaintext, cipher_key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Preserve the case of the letter
            is_upper = char.isupper()
            char = char.upper()
            # Use the monoalphabetic substitution key
            encrypted_char = cipher_key.get(char, char)
            ciphertext += encrypted_char.upper() if is_upper else encrypted_char.lower()
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, cipher_key):
    # To decrypt, we create a reverse key
    reverse_key = {v: k for k, v in cipher_key.items()}
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Preserve the case of the letter
            is_upper = char.isupper()
            char = char.upper()
            # Use the reverse monoalphabetic substitution key
            decrypted_char = reverse_key.get(char, char)
            plaintext += decrypted_char.upper() if is_upper else decrypted_char.lower()
        else:
            plaintext += char
    return plaintext

def main():
    # Example usage
    cipher_key = generate_cipher_key()
    print("Generated Monoalphabetic Substitution Key:")
    print(cipher_key)

    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt(plaintext, cipher_key)
    print(f"Encrypted text: {ciphertext}")

    decrypted_text = decrypt(ciphertext, cipher_key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()