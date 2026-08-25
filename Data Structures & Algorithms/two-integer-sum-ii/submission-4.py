class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i, len(numbers)-1
            curr = target - numbers[i]
            while l<=r:
                mid = (l+r)//2
                if curr==numbers[mid]:
                    return [i+1, mid+1]
                elif curr>numbers[mid]:
                    l = mid+1
                else:
                    r = mid - 1
