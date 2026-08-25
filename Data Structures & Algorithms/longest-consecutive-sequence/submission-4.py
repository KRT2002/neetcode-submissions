class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 0
        curr, streak = nums[0], 0
        index = 0

        while index < len(nums):
            if curr != nums[index]:
                curr = nums[index]
                streak = 0
            
            while index < len(nums) and curr==nums[index]:
                index += 1
            
            curr += 1
            streak += 1
            res = max(res, streak)
        
        return res