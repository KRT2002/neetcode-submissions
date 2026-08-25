class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        if nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(len(nums)):
            
            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.add(tuple([nums[i],nums[l],nums[r]]))
                    l += 1
                    r -= 1
        return [list(i) for i in res]
            