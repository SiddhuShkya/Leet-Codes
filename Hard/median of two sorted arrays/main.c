#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int size = nums1Size + nums2Size;
    int* mergedArr = malloc(size * sizeof(int));
    int i1 = 0;
    int i2 = 0;
    int i = 0;
    while (i < size) {
        if (nums1[i1] < nums2[i2]) {
            mergedArr[i] = nums1[i1];
            i1++;
            i++;
        }
        else {
            mergedArr[i] = nums2[i2];
            i2++;
            i++;
        }
    }
    if (size % 2 == 1) {
        return mergedArr[size / 2];
    }
    else {
        double res;
        int l = size / 2;
        int r = size / 2 + 1;
        res = (double)(l + r) / 2;
        return res;
    }
}

int main() {
    int nums1[] = { 1, 2 };
    int nums2[] = { 3, 4 };
    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    int size2 = sizeof(nums2) / sizeof(nums2[0]);
    double res = findMedianSortedArrays(nums1, size1, nums2, size2);
    printf("%f", res);
    return 0;
}