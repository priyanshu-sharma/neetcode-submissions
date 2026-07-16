class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        product = 1
        checked = False
        checked_count = 0
        while i < len(nums):
            if nums[i] not in [0, 1]:
                product *= nums[i]
            if nums[i] == 0:
                checked = True
                checked_count += 1
            i += 1
        values = []
        for i in range(0, len(nums)):
            if checked:
                if checked_count == 1 and nums[i] == 0:
                    data = product
                else:
                    data = 0
            else:
                if nums[i] == 1:
                    data = product
                else:
                    data = product // nums[i]
            values.append(data)
        return values