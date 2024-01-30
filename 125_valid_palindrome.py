# Higher performance, but pretty sure question not meant to be solved this way
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        clean_string = [i for i in s if i.isalnum()]
        return clean_string == clean_string[::-1]


# Lower performance, doesn't utilize python functions as heavily
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1


        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
