# My brute force, with some optimization. Passed 53/60 something cases

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        tallest_l = 0
        tallest_r = 0
        for i in range(len(height)):

            if height[i] < tallest:
                continue 

            tallest = height[i]
            for j in range(i, len(height)):
                
                bin_height = min(height[i], height[j])
                max_area = max((bin_height * (j-i)), max_area)
                j += 1

        return max_area

# More optimal solution    

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1

        while l < r:
            max_area = max((min(height[l], height[r]) * (r-l)), max_area)
            if height[l] <  height[r]:
                l += 1
            else:
                r -= 1  

        return max_area