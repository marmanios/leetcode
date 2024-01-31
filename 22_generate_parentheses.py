class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(stack))
                return
            
            elif open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()
            
            elif closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()
        
        backtrack(0,0)
        return res