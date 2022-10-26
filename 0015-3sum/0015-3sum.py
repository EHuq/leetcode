class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == [0,0,0]:
            return [[0,0,0]]
        nums.sort()
        length, result = len(nums), []
        for i in range(length):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            target = nums[i]*-1
            end, start = length-1, i+1
            while (end > start):
                if (nums[end] + nums[start] == target):
                    result.append([nums[end], nums[start], nums[i]])
                    start += 1
                    while (start < end and nums[start] == nums[start-1]):
                        start += 1
                elif (nums[end] + nums[start] < target):
                    start += 1
                else:
                    end -= 1
        return result