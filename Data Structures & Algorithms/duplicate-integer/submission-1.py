class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in count_dict.keys():
                count_dict[nums[i]] = 1
            else:
                return True
        return False