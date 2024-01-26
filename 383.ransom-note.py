#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter not in magazine:
                return False
            magazine = magazine.replace(letter, ' ', 1)
        return True
# @lc code=end

