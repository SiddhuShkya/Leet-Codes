#include <stdio.h>
#include <stdlib.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

char* getBinaryString(struct ListNode* head) {
    int size = 1;
    char* binaryStr = malloc(size * sizeof(char));
    if (!binaryStr) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    
    int i = 0;
    while (head) {
        binaryStr = realloc(binaryStr, (i + 2) * sizeof(char));  // +2 for the new character and the null terminator
        if (!binaryStr) {
            printf("Memory allocation failed\n");
            return NULL;
        }
        binaryStr[i] = head->val + '0';  // Convert integer 0/1 to character '0'/'1'
        head = head->next;
        i++;
    }
    binaryStr[i] = '\0';  // Null-terminate the string
    return binaryStr;
}

int getDecimalValue(struct ListNode* head) {
    int res = 0;
    int c = 1;  // Start with 1, as binary starts from the least significant bit

    char *bStr = getBinaryString(head);
    if (!bStr) {
        return -1;  // In case memory allocation failed
    }

    // Calculate the length of the binary string
    int size = 0;
    char *ptr = bStr;
    while (*ptr != '\0') {
        size++;
        ptr++;
    }

    // Convert the binary string to decimal
    for (int i = size - 1; i >= 0; i--) {
        if (bStr[i] == '1') {
            res += c;
        }
        c *= 2;  // Move to the next power of 2
    }

    free(bStr);  // Free the allocated memory for the binary string
    return res;
}

int main(){
    struct ListNode n5 = {1, NULL};
    struct ListNode n4 = {1, &n5};
    struct ListNode n3 = {1, &n4};
    struct ListNode n2 = {0, &n3};
    struct ListNode n1 = {1, &n2};
    int res = getDecimalValue(&n1);
    printf("res = %d\n", res);
    return 0;
}