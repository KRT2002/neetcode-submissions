class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        res = [1]*len_
        prefix = 1

        for i in range(len_):
            res[i]=prefix
            prefix*=nums[i]
        
        postfix = 1
        for i in range(len_-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res