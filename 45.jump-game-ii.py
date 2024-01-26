#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        curjump = 0
        curend = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(nums[0], farthest)
            if i == curend:
                curjump += 1
                curend = farthest
        return curjump        
# @lc code=end

