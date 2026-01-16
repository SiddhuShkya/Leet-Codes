def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    mergedArr = sorted(nums1 + nums2)
    if (m+n) % 2 == 1:
        return mergedArr[(m+n)//2]
    else:
        left_mid_idx = (m+n)//2 - 1
        right_mid_idx = (m+n)//2 
        return (float(mergedArr[left_mid_idx]) + float(mergedArr[right_mid_idx]))/2.0

print(findMedianSortedArrays([1, 2], [3, 4]))
