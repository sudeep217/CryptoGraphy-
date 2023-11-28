#include <stdio.h>
#include <stdlib.h>
#define MOD 26

void matrix_mod_inverse(int key[2][2], int inverse[2][2]) {
    int det = (key[0][0] * key[1][1] - key[0][1] * key[1][0] + MOD) % MOD;
    int det_inv;
    for (det_inv = 0; det_inv < MOD; det_inv++) {
        if ((det * det_inv) % MOD == 1) {
            break;
        }
    }
    inverse[0][0] = (key[1][1] * det_inv) % MOD;
    inverse[0][1] = (-key[0][1] * det_inv) % MOD;
    inverse[1][0] = (-key[1][0] * det_inv) % MOD;
    inverse[1][1] = (key[0][0] * det_inv) % MOD;
    if (inverse[0][1] < 0) {
        inverse[0][1] += MOD;
    }
    if (inverse[1][0] < 0) {
        inverse[1][0] += MOD;
    }
}

void hill_cipher_encrypt(char *plaintext, int key[2][2]) {
    int len = 2;
    int ciphertext[len];
    for (int i = 0; i < len; i += 2) {
        ciphertext[i] = (key[0][0] * (plaintext[i] - 'A') + key[0][1] * (plaintext[i + 1] - 'A')) % MOD;
        ciphertext[i + 1] = (key[1][0] * (plaintext[i] - 'A') + key[1][1] * (plaintext[i + 1] - 'A')) % MOD;
    }
    for (int i = 0; i < len; i++) {
        printf("%c", ciphertext[i] + 'A');
    }
    printf("\n");
}

void hill_cipher_decrypt(char *ciphertext, int key[2][2]) {
    int len = 2;
    int inverse[2][2];
    matrix_mod_inverse(key, inverse);
    int plaintext[len];
    for (int i = 0; i < len; i += 2) {
        plaintext[i] = (inverse[0][0] * (ciphertext[i] - 'A') + inverse[0][1] * (ciphertext[i + 1] - 'A')) % MOD;
        plaintext[i + 1] = (inverse[1][0] * (ciphertext[i] - 'A') + inverse[1][1] * (ciphertext[i + 1] - 'A')) % MOD;
    }
    for (int i = 0; i < len; i++) {
        printf("%c", plaintext[i] + 'A');
    }
    printf("\n");
}

int main() {
    char plaintext[3];
    int key[2][2];
    printf("Enter the 2x2 encryption key matrix (e.g., '6 24 13 16'): ");
    scanf("%d %d %d %d", &key[0][0], &key[0][1], &key[1][0], &key[1][1]);
    printf("Enter the 2-letter plaintext (uppercase): ");
    scanf("%s", plaintext);
    printf("Original Text: %s\n", plaintext);
    printf("Encrypted Text: ");
    hill_cipher_encrypt(plaintext, key);
    char ciphertext[] = "BTYE";
    printf("Decrypted Text: ");
    hill_cipher_decrypt(ciphertext, key);
    return 0;
}
