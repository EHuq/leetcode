#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)
        for i, citation in enumerate(citations):
            if citation < i + 1:
                return i
        return len(citations) 
# @lc code=end

