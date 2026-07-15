class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_dict.keys():
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        snums_dict = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
        return list(snums_dict.keys())[:k]