#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_good_index = n - 1
        index = last_good_index - 1
        while index > -1:
            if index + nums[index] >= last_good_index:
                last_good_index = index
            index -= 1
        
        return last_good_index == 0
            
        
# @lc code=end

