class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_count = {}
        for i in range(0, len(nums)):
            if nums[i] not in data_count.keys():
                data_count[nums[i]] = 1
            else:
                data_count[nums[i]] += 1
        output_list = []
        sorted_dict = dict(sorted(data_count.items(), key=lambda item: item[1], reverse=True))
        keys_list = list(sorted_dict.keys())
        values_list = list(sorted_dict.values())
        for i in range(0, k):
            output_list.append(keys_list[0])
            keys_list.pop(0)
            values_list.pop(0)
        return output_list