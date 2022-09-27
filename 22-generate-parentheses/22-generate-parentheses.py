class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def recurse(combo = [], left = 0, right = 0):
            if (len(combo) == 2*n):
                ans.append(''.join(combo))
                return
            if left < n:
                combo.append('(')
                recurse(combo, left+1, right)
                print(combo, '1')
                combo.pop()
                print(combo, '1.1')
            if right < left:
                combo.append(')')
                recurse(combo, left, right+1)
                print(combo, '2')
                combo.pop()
                print(combo, '2.1')
        
        recurse()
        return ans
                