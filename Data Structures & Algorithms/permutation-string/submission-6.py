class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        countS1 = {}

        for i in range(len(s1)):
            countS1[s1[i]] = countS1.get(s1[i], 0) + 1
        
        # Calculate number of unique keys/characters
        need = len(countS1)

        for i in range(len(s2)):
            countS2, curr = {}, 0
            for j in range(i, len(s2)):
                countS2[s2[j]] = countS2.get(s2[j], 0) + 1
                if countS1.get(s2[j], 0) < countS2[s2[j]]:
                    break
                if countS1.get(s2[j], 0) == countS2[s2[j]]:
                    curr += 1
                if curr == need:
                    return True
        return False