class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_of = {}
        for i in range(len(nums)):
            if (target - nums[i]) in index_of:
                return [index_of[target-nums[i]], i] 
                
            index_of[nums[i]] = i

        