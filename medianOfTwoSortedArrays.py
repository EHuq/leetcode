#MedianOfTwoSortedArrays [HARD] 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1 = sorted(nums1)

        if len(nums1) % 2:
            return float(nums1[len(nums1)//2])
        else:
            ans = nums1[(len(nums1)//2)-1], nums1[len(nums1)//2]
            return sum(ans)/2