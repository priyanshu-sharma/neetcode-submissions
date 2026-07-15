class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''
        for i in s:
            if i.isalnum():
                k += i
        k = k.lower()
        i, j = 0, len(k) - 1
        while i < j:
            if k[i] == k[j]:
                i += 1
                j -= 1
            else:
                return False
        return True