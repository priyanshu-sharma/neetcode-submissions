class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num not in count_dict.keys():
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        freq = len(nums)//2
        for key, value in count_dict.items():
            if value > freq:
                return key
        return -1