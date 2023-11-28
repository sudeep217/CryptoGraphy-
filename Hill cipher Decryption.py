import string

main = string.ascii_lowercase

def generate_key(n, s):
    s = s.replace(" ", "")
    s = s.lower()

    key_matrix = ['' for i in range(n)]
    i = 0
    j = 0
    for c in s:
        if c in main:
            key_matrix[i] += c
            j += 1
            if j > n - 1:
                i += 1
                j = 0
    print("The key matrix " + "(" + str(n) + 'x' + str(n) + ") is:")
    print(key_matrix)

    key_num_matrix = []
    for i in key_matrix:
        sub_array = []
        for j in range(n):
            sub_array.append(ord(i[j]) - ord('a'))
        key_num_matrix.append(sub_array)

    for i in key_num_matrix:
        print(i)
    return key_num_matrix

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def method(a, m):
    if a > 0:
        return a % m
    else:
        k = (abs(a) // m) + 1
    return method(a + k * m, m)

def message_matrix(s, n):
    s = s.replace(" ", "")
    s = s.lower()
    final_matrix = []
    if len(s) % n != 0:
        for i in range(abs(len(s) % n)):
            s = s + 'z'
    print("Converted cipher_text for decryption: ", s)
    for k in range(len(s) // n):
        message_matrix = []
        for i in range(n):
            sub = []
            for j in range(1):
                sub.append(ord(s[i + (n * k)]) - ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("The column matrices of plain text in numbers are:  ")
    for i in final_matrix:
        print(i)
    return final_matrix

def multiply_and_convert(key, message):
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)

    return res_alpha

def calculate_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            det += ((-1) ** i) * matrix[0][i] * calculate_determinant(submatrix)
        return det

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse_matrix(matrix, mod):
    det = calculate_determinant(matrix)
    det_inv = mod_inverse(det, mod)
    
    cofactors = [[(((-1) ** (i + j)) * calculate_determinant([row[:i] + row[i+1:] for row in (matrix[:j] + matrix[j+1:])])) % mod for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    adjoint = transpose(cofactors)
    inverse = [[(det_inv * adjoint[i][j]) % mod for j in range(len(adjoint[0]))] for i in range(len(adjoint))]
    
    return inverse

n = int(input("What will be the order of square matrix: "))
s = input("Enter the key: ")
key_matrix = generate_key(n, s)

det = calculate_determinant(key_matrix)
adjoint = inverse_matrix(key_matrix, 26)

if det != 0:
    convert_det = mod_inverse(det, 26)

    print("Adjoint Matrix after modulo 26 operation:")
    for i in adjoint:
        print(i)

    inverse = [[(convert_det * adjoint[i][j]) % 26 for j in range(len(adjoint[0]))] for i in range(len(adjoint))]
    
    print("Inverse matrix after applying modulo 26 operation:")
    for i in inverse:
        print(i)

    cipher_text = input("Enter the cipher text: ")
    message = message_matrix(cipher_text, n)
    plain_text = ''
    for i in message:
        sub = multiply_and_convert(inverse, i)
        for j in sub:
            for k in j:
                plain_text += k

    print("Plain message:", plain_text)
else:
    print("Matrix cannot be inverted")