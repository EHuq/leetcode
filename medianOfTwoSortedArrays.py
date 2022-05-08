#MedianOfTwoSortedArrays [HARD] 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        arr = sorted(nums1)
        n=len(arr)
        m=n//2
        if(n%2==0):
            s=(arr[m-1]+arr[m])/2
        else:
            s=arr[m]
        return s