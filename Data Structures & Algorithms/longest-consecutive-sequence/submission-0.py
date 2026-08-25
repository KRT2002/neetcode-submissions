class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0

        for i in range(len(nums)):
            if nums[i]-1 in nums_set:
                continue
            temp=0
            while nums[i]+temp in nums_set:
                temp+=1
            count = max(count, temp)
            
        return count