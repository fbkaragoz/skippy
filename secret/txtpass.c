#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/* 
 * SECURITY WARNING: This file contains insecure authentication and file handling
 * - Hardcoded password is not secure
 * - tokens.txt should not contain plaintext API keys
 * - Use proper authentication and secret management instead
 */

const char* storedPasswordHash = "555";
const char* encryptedFilePath = "../api/info/tokens.txt"; 

bool authenticatedUser() {
    char enteredPassword[100];
    printf("Enter the password: ");
    scanf("%s", enteredPassword);

    if (strcmp(storedPasswordHash, enteredPassword) == 0) {
        return true;
    } else {
        return false;
    }
}

int main() {
    if (authenticatedUser()) {
        FILE* encryptedFile = fopen(encryptedFilePath, "r");

        if (encryptedFile == NULL) {
            printf("Error opening the file.\n");
            return 1;
        }

        char decryptedContent[1000];

        while (fgets(decryptedContent, sizeof(decryptedContent), encryptedFile) != NULL) {
        }

        printf("Decrypted content: \n%s\n", decryptedContent);

        fclose(encryptedFile);
    } else {
        printf("Authentication failed.\n");
    }
    return 0;
}
