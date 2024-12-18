#include <stdio.h>
#include <stdlib.h>

int countPairs(int* nums, int numsSize, int target) {
    int res = 0;
    for (int i = 0; i < numsSize; i++){
        for (int j = i + 1; j < numsSize; j++){
            if (nums[i] + nums[j] < target){
                res += 1;
            }
        }
    }
    return res;
}