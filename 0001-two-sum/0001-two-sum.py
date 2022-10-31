class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = dict()
        for i in range(len(nums)):
            if (target-nums[i] in complements):
                return [nums.index(target-nums[i]), i]
            else:
                complements[nums[i]] = 1