class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for index in range(len(numbers)):
            prev = target - numbers[index]
            if prev in hashmap:
                return [hashmap[prev]+1, index+1]
            hashmap[numbers[index]]=index