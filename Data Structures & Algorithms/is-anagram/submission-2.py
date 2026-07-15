class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i in s_dict.keys():
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        t_dict = {}
        for i in t:
            if i in t_dict.keys():
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        if len(s_dict.keys()) != len(t_dict.keys()):
            return False
        if len(s_dict.values()) != len(t_dict.values()):
            return False
        for key, value in s_dict.items():
            if key not in t_dict.keys():
                return False
            if t_dict[key] != value:
                return False
        return True