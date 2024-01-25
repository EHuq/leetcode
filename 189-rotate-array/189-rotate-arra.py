class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if k == 0:
            return
        k = k % len(nums)
        if k == len(nums):
            return 
        
        nums[:] = nums[-k:] + nums[:-k]
        