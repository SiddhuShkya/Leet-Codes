#include <stdio.h>
#include <stdlib.h>

// Define the struct for the hashmap (key-value pair)
struct hashmap {
    int key;   // The number from the array (nums[i])
    int value; // The index of the number (i)
};

// Helper function to find the value in the hashmap
int findInHashMap(struct hashmap* map, int size, int key) {
    for (int i = 0; i < size; i++) {
        if (map[i].key == key) {
            return map[i].value; // Return the index if the key is found
        }
    }
    return -1; // Return -1 if the key is not found
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Allocate memory for storing the result (2 indices)
    int *res = (int*) malloc(2 * sizeof(int));
    
    // Hashmap to store the numbers and their indices
    struct hashmap *map = (struct hashmap*) malloc(numsSize * sizeof(struct hashmap));
    int mapSize = 0; // Current size of the hashmap
    
    // Traverse the array to find two numbers that sum to target
    for (int i = 0; i < numsSize; i++) {
        int diff = target - nums[i];
        
        // Check if the complement (diff) is already in the hashmap
        int idx = findInHashMap(map, mapSize, diff);
        if (idx != -1) {
            // If complement is found, return the indices
            res[0] = idx;
            res[1] = i;
            *returnSize = 2;
            free(map); // Free the hashmap memory
            return res;
        }
        
        // Otherwise, add the current number and its index to the hashmap
        map[mapSize].key = nums[i];
        map[mapSize].value = i;
        mapSize++;
    }
    
    // If no solution is found, set returnSize to 0 and return NULL
    *returnSize = 0;
    free(map); // Free the hashmap memory
    return NULL;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;

    // Call the twoSum function
    int* result = twoSum(nums, numsSize, target, &returnSize);
    
    if (result != NULL) {
        printf("Indices: %d, %d\n", result[0], result[1]);
    } else {
        printf("No solution found\n");
    }
    
    // Free the allocated memory
    free(result);

    return 0;
}
