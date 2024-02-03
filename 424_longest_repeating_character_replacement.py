
def characterReplacement(s: str, k: int) -> int:
    ans, largest_count, left, right = 0, 0, 0, 0
    counts = {}

    while right < len(s):
        counts[s[right]] = counts.get(s[right],0) + 1
        largest_count = max(largest_count, counts[s[right]]) 

        if (right - left + 1) - largest_count > k:
            counts[s[left]] = counts[s[left]] - 1
            left += 1
        else:
            ans = max(ans, right - left + 1)

        right += 1 
    
    return ans