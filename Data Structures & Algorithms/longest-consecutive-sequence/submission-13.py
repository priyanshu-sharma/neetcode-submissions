class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        ls = 1
        max_ls = -10
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            print(nums)
            while i < len(nums):
                if nums[i] - nums[i-1] == 1:
                    ls += 1
                elif nums[i] - nums[i-1] > 1:
                    if ls >= max_ls:
                        max_ls = ls
                    ls = 1
                i += 1
            return max(max_ls, ls)