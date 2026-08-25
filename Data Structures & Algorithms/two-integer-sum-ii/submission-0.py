class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rear, front = len(numbers) - 1, 0

        while rear>front:
            if numbers[rear]+numbers[front] > target:
                rear-=1
            elif numbers[rear]+numbers[front] < target:
                front+=1
            else:
                return [front+1, rear+1]