class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counts = dict()
        for num in nums: 
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return max(counts, key=counts.get)