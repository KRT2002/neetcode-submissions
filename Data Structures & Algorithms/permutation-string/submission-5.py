class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        need = len(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i:j+1]
                if len(subStr) > need:
                    break
                if s1 == sorted(subStr):
                    return True
        return False