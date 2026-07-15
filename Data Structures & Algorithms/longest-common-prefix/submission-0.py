class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = 1000
        for strns in strs:
            if len(strns) < mini:
                mini = len(strns)

        common = 0
        for i in range(0, mini):
            count = 0
            for j in range(1, len(strs)):
                if strs[0][i] == strs[j][i]:
                    count += 1
            if count == len(strs) - 1:
                common += 1
                continue
            else:
                return strs[0][:common]
        return strs[0][:common]
