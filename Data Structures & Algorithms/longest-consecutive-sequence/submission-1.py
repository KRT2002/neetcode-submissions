class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        lcs = 0

        for num in nums:
            curr = num
            streak = 0
            while curr in store:
                curr+=1
                streak+=1
            lcs = max(lcs, streak)
        
        return lcs
