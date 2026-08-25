class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        length_nums = len(nums)

        for index in range(length_nums):
            if index!=0:
                prefix = prefix*nums[index-1]
            result.append(prefix)
        
        postfix = 1
        for index in range(length_nums-1, -1, -1):
            if index!=length_nums-1:
                postfix*=nums[index+1]
            res = result[index]*postfix
            result[index]=res
        return result

        