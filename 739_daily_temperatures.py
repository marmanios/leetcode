# My solution is terrible 
class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Stores the lowest index at where u can find a temp higher than this
        index_at_temp = {}
        res = []
        for i in range (30, 81): index_at_temp[i] = 0

        for i in range(len(temperatures)-1, -1 , -1):

            # set the index of every temp lower than the one found
            # to the current index
            s = temperatures[i] - 1 
            for j in range(s, 29, -1):
                index_at_temp[j] = i


            res.append(max(index_at_temp.get(temperatures[i], 0)-i, 0))
        return res[::-1]


# This one is better. Go through the temps, store the indexes on a stack
# while the current temp is higher than one on the stack, pop and update the temp=
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(T)
        stack = []
        for curr_day in range(len(T)):
            while stack and T[curr_day] > T[stack[-1]]:
                prev = stack.pop()
                days_passed = curr_day - prev
                res[prev] = days_passed
            stack.append(curr_day)

        return res