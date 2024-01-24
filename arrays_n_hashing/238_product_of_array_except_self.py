class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        zero_count = 0
        result = []

        for i, val in enumerate(nums):
            if val == 0:
                zero_count += 1
            else:
                total *= val

        if zero_count > 1:
            return [0 for i in range(len(nums))]
        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    result.append(total)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(int(total/num))

        return result