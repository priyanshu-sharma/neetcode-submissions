class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [i for i in s]
        final = ''
        for i in range(0, len(s_list)):
            if s_list[i].isalnum():
                final += s_list[i].lower()
        i, j = 0, len(final) - 1
        while i <= j:
            if final[i] != final[j]:
                return False
            else:
                i += 1
                j -= 1
        return True