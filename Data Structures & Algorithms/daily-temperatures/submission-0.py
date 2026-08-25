class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            counter = 0
            for j in range(i+1, len(temperatures)):
                counter += 1
                if temperatures[i] < temperatures[j]:
                    result[i]=counter
                    break
        
        return result