#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isValid(char* s) {
    int size = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        size++;
    }
    char* stack = malloc(size * sizeof(char));
    int top = -1;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            top++;
            stack[top] = c;
        }
        else if (c == ')' || c == ']' || c == '}') {
            if (top == -1 || (c == ')' && stack[top] != '(') ||
                (c == ']' && stack[top] != '[') || (c == '}' && stack[top] != '{')) {
                return false;
            }
            top--;
        }
    }
    return top == -1;
}

int main() {
    char* str = "{[()]}";
    if (isValid(str)) {
        printf("Is Valid");
        return 0;
    }
    printf("Is Not Valid");
    return 0;
}