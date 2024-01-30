class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_found = set()
        for num in nums:
            if num in nums_found:
                return True
            nums_found.add(num)
        
        return False