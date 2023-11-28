def generate_key_square(key):
    key = key.upper().replace('J', 'I')
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = [list(key_set)] + [list(set(alphabet) - key_set)]
    return key_square
def find_char_positions(key_square, char):
    for i, row in enumerate(key_square):
        if char in row:
            return i, row.index(char)
def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = plaintext.upper().replace('J', 'I')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    encrypted_text = ""
    for pair in pairs:
        (row1, col1), (row2, col2) = find_char_positions(key_square, pair[0]), find_char_positions(key_square, pair[1])
        if row1 == row2:
            encrypted_text += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_square[(row1 + 1) % 2][col1] + key_square[(row2 + 1) % 2][col2]
        else:
            encrypted_text += key_square[row1][col2] + key_square[row2][col1]
    return encrypted_text
def main():
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    encrypted_text = playfair_encrypt(plaintext, key)
    print(f"Encrypted text: {encrypted_text}")
if __name__ == "__main__":
    main()