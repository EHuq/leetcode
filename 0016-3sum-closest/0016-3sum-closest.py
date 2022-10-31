class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        N = len(nums)
        for i in range(N):
            s, e = i+1, N-1
            while (s < e and s > 0):
                addition = nums[s] + nums[e] + nums[i]
                if (addition == target):
                    return addition
                elif (addition > target):
                    if (abs(addition - target) < abs(closest - target)):
                        closest = addition
                    e-=1
                else:
                    if (abs(addition - target) < abs(closest - target)):
                        closest = addition
                    s += 1
            while(i < len(nums)-1 and nums[i] == nums[i+1]):
                i+=1
        return closest
                    
        