def matrix_mod_inverse(matrix, modulus):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det %= modulus
    det_inv = pow(det, -1, modulus)  # Modular inverse of determinant

    adjugate = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    for i in range(2):
        for j in range(2):
            adjugate[i][j] %= modulus

    inverse_matrix = [[(det_inv * adjugate[i][j]) % modulus for j in range(2)] for i in range(2)]

    return inverse_matrix

def hill_cipher_encrypt(plaintext, key):
    key_size = int(len(key) ** 0.5)
    
    # Convert plaintext to numbers (A=0, B=1, ..., Z=25)
    plaintext = [ord(char) - ord('A') for char in plaintext.upper()]

    # Pad the plaintext if its length is not a multiple of the key size
    padding = (key_size - len(plaintext) % key_size) % key_size
    plaintext += [padding] * padding

    # Reshape the plaintext and key into matrices
    plaintext_matrix = [[plaintext[i * key_size + j] for j in range(key_size)] for i in range(len(plaintext) // key_size)]
    key_matrix = [[ord(char) - ord('A') for char in key.upper()][i * key_size:(i + 1) * key_size] for i in range(key_size)]

    # Perform the encryption using matrix multiplication
    ciphertext_matrix = [[sum(plaintext_matrix[i][k] * key_matrix[k][j] for k in range(key_size)) % 26 for j in range(key_size)] for i in range(len(plaintext) // key_size)]

    # Convert the encrypted matrix back to a list of numbers
    ciphertext = [char for row in ciphertext_matrix for char in row]

    # Convert numbers back to characters
    ciphertext = ''.join(chr(char + ord('A')) for char in ciphertext)

    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
    key_size = int(len(key) ** 0.5)
    
    # Convert ciphertext to numbers (A=0, B=1, ..., Z=25)
    ciphertext = [ord(char) - ord('A') for char in ciphertext.upper()]

    # Reshape the ciphertext into a matrix
    ciphertext_matrix = [[ciphertext[i * key_size + j] for j in range(key_size)] for i in range(len(ciphertext) // key_size)]

    # Convert the key to a matrix
    key_matrix = [[ord(char) - ord('A') for char in key.upper()][i * key_size:(i + 1) * key_size] for i in range(key_size)]

    # Calculate the inverse of the key matrix
    key_inverse = matrix_mod_inverse(key_matrix, 26)

    # Perform the decryption using matrix multiplication
    plaintext_matrix = [[sum(ciphertext_matrix[i][k] * key_inverse[k][j] for k in range(key_size)) % 26 for j in range(key_size)] for i in range(len(ciphertext) // key_size)]

    # Convert the decrypted matrix back to a list of numbers
    plaintext = [char for row in plaintext_matrix for char in row]

    # Remove padding and convert numbers back to characters
    plaintext = ''.join(chr(char + ord('A')) for char in plaintext if char != 23)

    return plaintext

def main():
    key = input("Enter the key (e.g., 'GYBNQKURP'): ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = hill_cipher_encrypt(plaintext, key)
    print(f"Encrypted text: {ciphertext}")

    decrypted_text = hill_cipher_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
