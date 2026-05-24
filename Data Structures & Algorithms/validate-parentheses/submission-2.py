from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for c in s:
            if c in "([{":
                q.append(c)
            if c in "}])":
                if len(q) == 0:
                    return False
                opened = q.pop()
                if c == "}" and opened != "{":
                   return False
                elif c == "]" and opened != "[":
                   return False
                elif c == ")" and opened != "(":
                   return False
        
        return len(q) == 0

        