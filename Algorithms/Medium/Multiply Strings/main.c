#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* multiply(char* num1, char* num2) {
    int num1_size = strlen(num1);
    int num2_size = strlen(num2);

    // Edge case: if either number is "0", the result is "0"
    if (strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0) {
        char* result = (char*)malloc(2);
        strcpy(result, "0");
        return result;
    }

    // Result array to store the multiplication result (max length is sum of lengths)
    int result_size = num1_size + num2_size;
    int* result = (int*)calloc(result_size, sizeof(int));

    // Multiply each digit from num1 by each digit from num2
    for (int i = num1_size - 1; i >= 0; i--) {
        for (int j = num2_size - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int sum = mul + result[i + j + 1];
            result[i + j] += sum / 10;
            result[i + j + 1] = sum % 10;
        }
    }

    // Find the starting index of the first non-zero digit in the result array
    int start_index = 0;
    while (start_index < result_size && result[start_index] == 0) {
        start_index++;
    }

    // Allocate memory for the result string
    char* result_str = (char*)malloc(result_size - start_index + 1);
    for (int i = start_index, j = 0; i < result_size; i++, j++) {
        result_str[j] = result[i] + '0';
    }
    result_str[result_size - start_index] = '\0'; // Null-terminate the string

    free(result); // Free the temporary result array
    return result_str;
}

int main() {
    char num1[] = "123";
    char num2[] = "456";
    char* result = multiply(num1, num2);
    printf("Result: %s\n", result);
    free(result); // Free the result after use
    return 0;
}
