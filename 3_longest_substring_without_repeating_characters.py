# My first attempt
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        size = len(s)
        while True:
            for i in range(len(s)-size+1):
                chars = set()
                for j in range(i, i + size):
                    if s[j] in chars:
                        break
                    chars.add(s[j])
                if len(chars) == size: return size

                
            size -= 1
        

# Optimal
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        arr = [-1] * 256

        max_len, start = 0, -1

        for i in range(len(s)):
            if arr[ord(s[i])] > start:
                start = arr[ord(s[i])]
            
            arr[ord(s[i])] = i

            max_len = max(max_len, i - start)
        return max_len