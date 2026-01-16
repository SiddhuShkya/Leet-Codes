#include <stdio.h>
#include <stdbool.h>
struct ListNode {
    int val;
    struct ListNode* next;
};

bool hasCycle(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return false; // If there are less than 2 nodes, no cycle can exist.
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;       // Move slow pointer one step at a time
        fast = fast->next->next; // Move fast pointer two steps at a time

        if (slow == fast) {
            return true; // If they meet, there is a cycle
        }
    }
    return false;
}

int main() {
    struct ListNode node1;
    struct ListNode node2;
    struct ListNode node3;
    struct ListNode node4;
    // Assign values to the nodes
    node1.val = 3;
    node2.val = 2;
    node3.val = 0;
    node4.val = 4;
    // Connect the nodes to create a linked list
    node1.next = &node2; // Use '&' to get the address of the node
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node2;   // Set the last node's next pointer to NULL to indicate the end of the list
    bool res = hasCycle(&node1);
    printf("%d", res);
    return 0;
}