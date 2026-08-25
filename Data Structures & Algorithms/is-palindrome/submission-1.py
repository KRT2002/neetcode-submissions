class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, rear = 0, len(s) - 1

        while front < rear:
            while front < rear and not self.isAlphaNumeric(s[front]):
                front += 1
            
            while rear > front and not self.isAlphaNumeric(s[rear]):
                rear -= 1

            if (s[front]).lower()!=(s[rear]).lower():
                return False
            
            front += 1
            rear -= 1
        
        return True


    def isAlphaNumeric(self, c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or 
        ord("a") <= ord(c) <= ord("z") or 
        ord("0") <= ord(c) <= ord("9"))
        