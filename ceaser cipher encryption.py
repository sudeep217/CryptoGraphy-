def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
plain_text = input("Enter the plain text:")
shift = int(input("Enter the shift key:"))
encrypted_text = encrypt_caesar(plain_text, shift)
print(f"Original Text: {plain_text}")
print(f"Encrypted Text: {encrypted_text}")