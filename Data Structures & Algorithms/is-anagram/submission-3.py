class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict.keys():
                s_dict[i] = 0
            else:
                s_dict[i] += 1
        
        for i in t:
            if i not in t_dict.keys():
                t_dict[i] = 0
            else:
                t_dict[i] += 1
        
        ss_dict = dict(sorted(s_dict.items()))
        tt_dict = dict(sorted(t_dict.items()))
        if len(ss_dict) == len(tt_dict) and list(ss_dict.keys()) == list(tt_dict.keys()) and list(ss_dict.values()) == list(tt_dict.values()):
            return True
        return False