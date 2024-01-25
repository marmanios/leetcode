class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        longest_sequence = 1
        i = 1
        while i < len(nums):
            j = i
            seq_length = 1
            while j < len(nums):
                if nums[j] == nums[j - 1] + 1:
                    seq_length += 1
                elif nums[j] != nums[j - 1]:
                    break
                
                j += 1
            
            if seq_length > longest_sequence:
                longest_sequence = seq_length

            i = j + 1

        return longest_sequence