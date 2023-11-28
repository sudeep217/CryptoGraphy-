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

def playfair_decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    ciphertext = ciphertext.upper().replace('J', 'I')

    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    decrypted_text = ""

    for pair in pairs:
        (row1, col1), (row2, col2) = find_char_positions(key_square, pair[0]), find_char_positions(key_square, pair[1])

        if row1 == row2:
            decrypted_text += key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_square[(row1 - 1) % 2][col1] + key_square[(row2 - 1) % 2][col2]
        else:
            decrypted_text += key_square[row1][col2] + key_square[row2][col1]
    return decrypted_text

def main():
    key = input("Enter the key: ")
    ciphertext = input("Enter the ciphertext: ")
    decrypted_text = playfair_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()