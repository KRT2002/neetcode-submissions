class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        
        if s1 == s2:
            return True
        
        s1_re = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i:j+1]
                subStr = sorted(subStr)
                if subStr == s1_re:
                    return True
        return False

