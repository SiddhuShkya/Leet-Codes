#include <stdio.h>

void singleNumber(int* nums, int numsSize) {
    int ones = 0, twos = 0;
    for (int i = 0; i < numsSize; i++) {
        ones = (ones ^ nums[i]) & ~twos;
        twos = (twos ^ nums[i]) & ~ones;
    }
    printf("%d\n", ones);
}

int main() {
    int nums[] = { 2, 2, 3, 2 };
    int size = sizeof(nums) / sizeof(nums[0]);
    singleNumber(nums, size);
    return 0;
}