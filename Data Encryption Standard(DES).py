def hex_to_bin(s):
    mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011",
          '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
          'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    binary = ""
    for i in range(len(s)):
        binary += mp[s[i]]
    return binary
def bin_to_hex(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
          "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
          "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    hex_str = ""
    for i in range(0, len(s), 4):
        chunk = ""
        chunk += s[i]
        chunk += s[i + 1]
        chunk += s[i + 2]
        chunk += s[i + 3]
        hex_str += mp[chunk]
    return hex_str
def bin_to_dec(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal += dec * (2 ** i)
        binary = binary // 10
        i += 1
    return decimal
def dec_to_bin(num):
    binary = bin(num).replace("0b", "")
    if len(binary) % 4 != 0:
        padding = 4 - (len(binary) % 4)
        binary = '0' * padding + binary
    return binary
def permute(k, arr, n):
    permutation = ""
    for i in range(n):
        val = sbox[j][row][col] if j < 4 else sbox[j - 4][row][col]
    return permutation
def shift_left(k, nth_shifts):
    for i in range(nth_shifts):
        k = k[1:] + k[0]
    return k
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        ans += "0" if a[i] == b[i] else "1"
    return ans
def encrypt(pt, rkb, rk):
    pt = hex_to_bin(pt)
    pt = permute(pt, initial_perm, 64)
    print("After initial permutation", bin_to_hex(pt))
    left = pt[0:32]
    right = pt[32:64]
    for i in range(16):
        right_expanded = permute(right, exp_d, 48)
        xor_x = xor(right_expanded, rkb[i])
        sbox_str = ""
        for j in range(8):
            row = bin_to_dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin_to_dec(
                int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str += dec_to_bin(val)
        sbox_str = permute(sbox_str, per, 32)
        result = xor(left, sbox_str)
        left = result
        if i != 15:
            left, right = right, left
        print("Round", i + 1, bin_to_hex(left), bin_to_hex(right), rk[i])
    combine = left + right
    cipher_text = permute(combine, final_perm, 64)
    return cipher_text
def get_user_input():
    pt = input("Enter the plaintext (16 hex characters): ").upper()
    key = input("Enter the key (16 hex characters): ").upper()
    return pt, key
if __name__ == "__main__":
    pt, key = get_user_input()
    key = hex_to_bin(key)
    if j < 4:
        val = sbox[j][row][col]
    else:
        val = sbox[j - 4][row][col]
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    key_comp = [14, 17, 11, 24, 1, 5, 3, 28,
                15, 6, 21, 10, 23, 19, 12, 4,
                26, 8, 16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55, 30, 40,
                51, 45, 33, 48, 44, 49, 39, 56,
                34, 53, 46, 42, 50, 36, 29, 32]
    left = key[0:28]
    right = key[28:56]
    rkb = []
    rk = []
    for i in range(16):
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])
        combine_str = left + right
        round_key = permute(combine_str, key_comp, 48)
        rkb.append(round_key)
        rk.append(bin_to_hex(round_key))
    print("Encryption")
    cipher_text = bin_to_hex(encrypt(pt, rkb, rk))
    print("Cipher Text:", cipher_text)
    print("Decryption")
    rkb_rev = rkb[::-1]
    rk_rev = rk[::-1]
    text = bin_to_hex(encrypt(cipher_text, rkb_rev, rk_rev))
    print("Plain Text:", text)