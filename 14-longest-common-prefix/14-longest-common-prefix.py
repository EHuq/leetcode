class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strng = ''
        for j in strs:
            strng += j
        diction = {}
        for j in strs:
            diction[j] = 0
            for k,l in enumerate(strng):
                try:
                    if j[k] == l:
                        diction[j] += 1
                    else:
                        break 
                except:
                    break
        return strng[0:min(diction.values())]