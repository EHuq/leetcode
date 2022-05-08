#MedianOfTwoSortedArrays [HARD] 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = sorted(nums1)
        return median(nums)
    