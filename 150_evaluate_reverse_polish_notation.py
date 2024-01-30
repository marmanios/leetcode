class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        nums = []
        for token in tokens:
            if token == "+":
                nums.append(nums.pop() + nums.pop())
            elif token == "-":
                nums.append(-1*nums.pop() + nums.pop())
            elif token == "*":
                nums.append(nums.pop() * nums.pop())
            elif token == "/":
                a, b = nums.pop(), nums.pop()
                nums.append(int(b / a))
            else:
                nums.append(int(token))

        return nums[0]
        