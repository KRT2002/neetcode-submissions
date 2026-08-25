class Solution:
    def isValid(self, s: str) -> bool:
        closedMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        open_stack = []
        index = 0

        while index < len(s):
            cur_char = s[index]
            
            if cur_char in closedMap:
                if not open_stack:
                    return False
                else:
                    elem = open_stack.pop()
                    if elem != closedMap[cur_char]:
                        return False
            else:
                open_stack.append(cur_char)
            index += 1
        
        return True if not open_stack else False
        