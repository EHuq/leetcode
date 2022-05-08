class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i in range(0, len(nums)):
            if ( (target-nums[i]) in complements):
                return [nums.index(target-nums[i]), i]
            else:
                complements[nums[i]] = 1
    