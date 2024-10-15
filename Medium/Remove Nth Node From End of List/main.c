#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int l = 0;
    struct ListNode *tmp1 = head;
    
    // Calculate the length of the list
    while (tmp1 != NULL) {
        l++;
        tmp1 = tmp1->next;
    }

    // Calculate the position of the node to remove from the start
    n = l - n;

    // Special case: removing the head node
    if (n == 0) {
        struct ListNode* newHead = head->next;
        return newHead;
    }

    // Traverse to the node before the one to be removed
    struct ListNode *tmp2 = head;
    while (n > 1) {  // Stop at the node before the one to be deleted
        tmp2 = tmp2->next;
        n--;
    }

    // Remove the nth node from the end
    struct ListNode *nodeToRemove = tmp2->next;
    tmp2->next = tmp2->next->next;  // Skip the node

    return head;
}

int main() {
    struct ListNode node1;
    struct ListNode node2;
    struct ListNode node3;
    struct ListNode node4;
    struct ListNode node5;

    node1.val = 1;
    node1.next = &node2;
    node2.val = 2;
    node2.next = &node3;
    node3.val = 3;
    node3.next = &node4;
    node4.val = 4;
    node4.next = &node5;
    node5.val = 5;
    node5.next = NULL;

    // Remove the 2nd node from the end
    struct ListNode *res = removeNthFromEnd(&node1, 2);

    // Print the updated list
    struct ListNode *current = res;
    while (current != NULL) {
        printf("Node value: %d\n", current->val);
        current = current->next;
    }

    return 0;
}
