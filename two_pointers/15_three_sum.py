# too slow. Need to add checks to ignore duplicates
# Another solution is the split up data into negs, zeros, and
# positive numbers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)-1):
            j = i+1
            k = len(nums) -1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    if [nums[i] ,nums[j] ,nums[k]] not in results:
                        results.append([nums[i] ,nums[j] ,nums[k]])
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k-=1
                else:
                    j+=1
                    
        return results
                    

        