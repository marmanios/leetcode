class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = {}
        
        # sort string
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in anagram_groups:
                anagram_groups[sorted_str].append(string)
            else:
                anagram_groups[sorted_str] = [string]
    
        return anagram_groups.values()
        