#MedianOfTwoSortedArrays [HARD] 
class Solution:
    def qsort(self, inlist):
        if inlist == []: 
            return []
        else:
            pivot = inlist[0]
            lesser = self.qsort([x for x in inlist[1:] if x < pivot])
            greater = self.qsort([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = self.qsort(nums1)
        return median(nums)
    