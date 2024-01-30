class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brkts = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for brkt in s:
            if brkt not in brkts:
                stack.append(brkt)
            elif not stack or brkts[brkt] != stack.pop():
                return False
        
        if not stack:
            return True 
        return False
        