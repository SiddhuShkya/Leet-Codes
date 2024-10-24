#include <stdio.h>

// Definition of a singly linked list node
struct ListNode {
    int val;                // Integer value of the node
    struct ListNode *next;  // Pointer to the next node in the list
};

// Function to swap adjacent pairs of nodes in the list
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode dummy = {0, head};  // A dummy node to make the logic simpler
    struct ListNode *prev, *curr;
    prev = &dummy;  // Set prev to point to the dummy node
    curr = head;    // Set curr to point to the head of the list

    // Iterate through the list while there are at least two nodes to swap
    while (curr != NULL && curr->next != NULL) {
        struct ListNode *nxt_pair = curr->next->next; // Pointer to the next pair
        struct ListNode *second_node = curr->next;    // Pointer to the second node in the current pair
        
        // Swap the two nodes in the current pair
        second_node->next = curr;
        curr->next = nxt_pair;
        prev->next = second_node;

        // Move the pointers forward to the next pair
        prev = curr;
        curr = nxt_pair;
    }

    // Return the new head of the list (dummy.next skips the dummy node)
    return dummy.next;
}

// Helper function to print the linked list
void printList(struct ListNode* head) {
    struct ListNode* curr = head;
    while (curr != NULL) {
        printf("%d -> ", curr->val);
        curr = curr->next;
    }
    printf("NULL\n");
}

int main() {
    // Create a linked list: 1 -> 2 -> 3 -> 4
    struct ListNode n4 = {4, NULL};
    struct ListNode n3 = {3, &n4};
    struct ListNode n2 = {2, &n3};
    struct ListNode n1 = {1, &n2};

    // Print original list
    printf("Original list:\n");
    printList(&n1);

    // Swap adjacent pairs
    struct ListNode* new_head = swapPairs(&n1);

    // Print the modified list
    printf("List after swapping pairs:\n");
    printList(new_head);

    return 0;
}
