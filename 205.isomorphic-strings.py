#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens = len(s) 
        lent = len(t) 
        if lens != lent:
            return False
        
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for ct, cs in zip(t, s):
            if ct in t_to_s_mapping and t_to_s_mapping[ct] != cs:
                return False
            
            if cs in s_to_t_mapping and s_to_t_mapping[cs] != ct:
                return False
            
            t_to_s_mapping[ct] = cs
            s_to_t_mapping[cs] = ct

        return True 
                
# @lc code=end

