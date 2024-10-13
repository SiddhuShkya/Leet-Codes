#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Allocate memory for storing the result (2 indices)
    int *res = (int*) malloc(2 * sizeof(int));
    
    // Traverse the array to find two numbers that sum to target
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                // If a solution is found, store the indices in res
                res[0] = i;
                res[1] = j;
                // Set returnSize to 2 since we are returning two indices
                *returnSize = 2;
                return res; // Return the result array
            }
        }
    }
    
    // If no solution is found, set returnSize to 0 and return NULL
    *returnSize = 0;
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
