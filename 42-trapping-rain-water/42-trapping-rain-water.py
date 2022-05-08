class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        left = 0
        right = len(height) - 1
        maxl = height[left]
        maxr = height[right]
        ret = 0
        
        while left < right:
            if maxl < maxr:
                left += 1
                maxl = max(maxl, height[left])
                ret += maxl - height[left]
            else:
                right -= 1
                maxr = max(maxr, height[right])
                ret += maxr - height[right]
        
        return ret
        