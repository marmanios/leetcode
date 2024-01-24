class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        hash_s = {}
        hash_t = {}

        if len_s != len_t: return False

        for i in range(len_s):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1
        
        for i in hash_s:
            if hash_s[i] != hash_t.get(i,0):
                return False

        return True