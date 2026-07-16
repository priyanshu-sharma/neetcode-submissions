class Solution:
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left <= right:
            mid = ( left + right + 1 ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binary_search(nums, left, mid - 1, target)
            elif nums[mid] < target:
                return self.binary_search(nums, mid + 1, right, target)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)