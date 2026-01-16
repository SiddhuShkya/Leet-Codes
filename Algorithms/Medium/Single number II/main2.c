#include <stdio.h>


int *sortArray(int *nums, int numsSize){
    for (int i = 0; i < numsSize - 1; i++){
        for (int j = 0; j < numsSize - i - 1; j++){
            int tmp;
            if (nums[j] > nums[j + 1]){
                tmp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = tmp;
            }
        }
    }
    return nums;
}


int singleNumber(int* nums, int numsSize) {
    int *sorted = sortArray(nums, numsSize);  
    for (int i = 0; i < numsSize - 1; i += 3) {
        if (sorted[i] != sorted[i + 1]) {
            return sorted[i];  
        }
    }
    return sorted[numsSize - 1];  
}


int main(){
    int nums[] = {0, 1, 0, 1, 0, 1, 99};
    int size = sizeof(nums)/sizeof(nums[0]);
    int res = singleNumber(nums, size);
    printf("res = %d\n", res);
    return 0;
}