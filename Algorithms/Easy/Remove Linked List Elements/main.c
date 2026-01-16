#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL) return NULL;  // Handle empty list case.

    struct ListNode *cur_node = head;
    
    while (cur_node->next != NULL) {
        if (cur_node->val == cur_node->next->val) {
            struct ListNode *duplicate_node = cur_node->next;
            cur_node->next = duplicate_node->next;  // Skip the duplicate node.
        } else {
            cur_node = cur_node->next;  // Move to the next node if no duplicate.
        }
    }
    return head;
}


int main(){
    struct ListNode node1;
    struct ListNode node2;
    struct ListNode node3;
    struct ListNode node4;
    struct ListNode node5;

    node1.val = 1;
    node1.next = &node2;
    node2.val = 2;
    node2.next = &node3;
    node3.val = 2;
    node3.next = &node4;
    node4.val = 4;
    node4.next = &node5;
    node5.val = 5;
    node5.next = NULL;

    // Print the initial list
    printf("Initial list:\n");
    struct ListNode *current = &node1;
    while (current != NULL) {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n");

    // Remove the 2nd node from the end
    struct ListNode *res = deleteDuplicates(&node1);

    // Print the updated list
    printf("Updated list after removal:\n");
    current = res;
    while (current != NULL) {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n");

    return 0;
}