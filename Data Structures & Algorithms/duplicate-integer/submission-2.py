class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for i in nums:
            if i in data.keys():
                return True
            else:
                data[i] = True
        return False