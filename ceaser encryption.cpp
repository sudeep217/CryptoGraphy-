#include <stdio.h>
#include <string.h>
void encrypt(char message[], int key) {
    int i;
    char encryptedMessage[100];
    for (i = 0; i < strlen(message); i++) {
        if (message[i] >= 'A' && message[i] <= 'Z') {
            encryptedMessage[i] = (message[i] + key - 'A') % 26 + 'A';
        }
        else if (message[i] >= 'a' && message[i] <= 'z') {
            encryptedMessage[i] = (message[i] + key - 'a') % 26 + 'a';
        }
        else {
            encryptedMessage[i] = message[i];
        }
    }
    encryptedMessage[i] = '\0'; // Null-terminate the encrypted string
    printf("Encrypted message: %s\n", encryptedMessage);
}
int main() {
    char message[100];
    int key;
	printf("Enter a message: ");
    fgets(message, sizeof(message), stdin);
    message[strcspn(message, "\n")] = '\0';
	printf("Enter the key (an integer): ");
    scanf("%d", &key);
    encrypt(message, key);
    return 0;
}
