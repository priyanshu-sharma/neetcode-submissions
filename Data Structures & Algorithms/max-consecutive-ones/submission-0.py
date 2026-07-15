class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = -1
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1

            if count > maxi:
                maxi = count
            
            if nums[i] == 0:
                count = 0
        return maxi