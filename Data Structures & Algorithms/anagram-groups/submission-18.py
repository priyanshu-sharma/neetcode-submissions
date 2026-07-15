class Solution:
    def get_frequency_dict(self, string_data: str) -> str:
        st_dict = {}
        for st in string_data:
            if st not in st_dict.keys():
                st_dict[st] = 1
            else:
                st_dict[st] += 1
        sst_dict = dict(sorted(st_dict.items()))
        return str(sst_dict)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        data = []
        for s in strs:
            data.append(self.get_frequency_dict(s))
        data_set = list(set(data))
        for i in range(0, len(data_set)):
            va = []
            for j in range(0, len(data)):
                if data_set[i] == data[j]:
                    va.append(strs[j])
            final.append(va)
        return final