#include <stdio.h>
// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;      // Dummy node to act as the start of the merged list
    struct ListNode* current = &dummy;  // Current pointer to build the merged list
    dummy.next = NULL;           // Initialize dummy’s next to NULL
    
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    // Attach the remaining list, if any
    if (list1 != NULL) {
        current->next = list1;
    } else {
        current->next = list2;
    }
    
    return dummy.next;  // Return the merged list starting from dummy’s next
}

// Helper function to print the list
void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("NULL\n");
}


int main(){
    struct ListNode list1_3 = {4, NULL};
    struct ListNode list1_2 = {2, &list1_3};
    struct ListNode list1_1 = {1, &list1_2};

    struct ListNode list2_3 = {4, NULL};
    struct ListNode list2_2 = {3, &list2_3};
    struct ListNode list2_1 = {1, &list2_2};

    // Merging the two lists
    struct ListNode* mergedList = mergeTwoLists(&list1_1, &list2_1);

    // Printing the merged list
    printf("Merged List: ");
    printList(mergedList);

    return 0;
}