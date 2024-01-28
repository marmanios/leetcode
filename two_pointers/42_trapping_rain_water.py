# my solution

class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        # Each index represents the tallest block to come
        tallest_upcomming = [0]
        for i in range(len(height)-2, -1, -1):
            tallest_upcomming.insert(0,max(tallest_upcomming[0],height[i + 1]))

        l = 0
        while l < len(height) -1:
            # Skip
            if height[l] == 0:
                l+=1
            
            # Start counting water stored
            else:
                sec_height = min(height[l], tallest_upcomming[l])
                r = l+1
                water_trapped = 0
                while height[r] < sec_height:
                    water_trapped += sec_height - height[r]
                    r += 1
                
                total_water += water_trapped
                l = r

        return total_water
    

## A 2 pointer sol'n
    
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        ans = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                ans += max(max_l-height[l], 0)
                max_l = max(max_l, height[l])

            else:
                r -= 1
                ans += max(max_r-height[r], 0)
                max_r = max(max_r, height[r])

        return ans 