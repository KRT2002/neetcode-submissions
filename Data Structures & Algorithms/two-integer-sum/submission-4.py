class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, elem in enumerate(nums):
            hashmap[elem] = index
        
        for index, elem in enumerate(nums):
            diff = target - elem
            if diff in hashmap and index!=hashmap[diff]:
                return [index, hashmap[diff]]