#include <stdio.h>
#include <string.h>
void decrypt(char encryptedMessage[], int key) {
    int i;
    char decryptedMessage[100];
    for (i = 0; i < strlen(encryptedMessage); i++) {
        if (encryptedMessage[i] >= 'A' && encryptedMessage[i] <= 'Z') {
            decryptedMessage[i] = (encryptedMessage[i] - key - 'A' + 26) % 26 + 'A';
        }
        else if (encryptedMessage[i] >= 'a' && encryptedMessage[i] <= 'z') {
            decryptedMessage[i] = (encryptedMessage[i] - key - 'a' + 26) % 26 + 'a';
        }
        else {
            decryptedMessage[i] = encryptedMessage[i];
        }
    }
    decryptedMessage[i] = '\0'; // Null-terminate the decrypted string
    printf("Decrypted message: %s\n", decryptedMessage);
}
int main() {
    char encryptedMessage[100];
    int key;
    printf("Enter an encrypted message: ");
    fgets(encryptedMessage, sizeof(encryptedMessage), stdin);
    encryptedMessage[strcspn(encryptedMessage, "\n")] = '\0';
    printf("Enter the key (an integer): ");
    scanf("%d", &key);
    decrypt(encryptedMessage, key);
    return 0;
}
