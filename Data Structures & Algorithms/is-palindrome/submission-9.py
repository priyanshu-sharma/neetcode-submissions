class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ds = ''
        for i in s:
            if i.isalnum():
                ds += i
        i = 0
        while i <= (len(ds) + 1) // 2:
            if i >= 0 and i < len(ds) and ds[i] != ds[len(ds) - 1 - i]:
                print(i, ds[i], ds[len(ds) - 1 - i])
                return False
            i += 1
        return True