class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod*=num
            else:
                zero_cnt+=1
        
        res = []
        for index, num in enumerate(nums):
            if zero_cnt>1:
                return [0]*len(nums)
            elif zero_cnt==1:
                if not num:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod/num))
        
        return res