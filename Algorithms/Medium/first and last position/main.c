#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int findFirstOccurrence(int *nums, int numsSize, int target) {
    int start = 0, end = numsSize - 1, result = -1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (nums[mid] == target) {
            result = mid; // Store the current index
            end = mid - 1; // Narrow the search to the left side
        } else if (nums[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return result;
}

int findLastOccurrence(int *nums, int numsSize, int target) {
    int start = 0, end = numsSize - 1, result = -1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (nums[mid] == target) {
            result = mid; // Store the current index
            start = mid + 1; // Narrow the search to the right side
        } else if (nums[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return result;
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int *result = malloc(2 * sizeof(int));
    *returnSize = 2; // The result array always has size 2

    if (numsSize == 0) {
        result[0] = -1;
        result[1] = -1;
        return result;
    }

    result[0] = findFirstOccurrence(nums, numsSize, target);
    result[1] = findLastOccurrence(nums, numsSize, target);

    return result;
}