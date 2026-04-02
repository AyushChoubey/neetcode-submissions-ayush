class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26}

        list_ = [0]*26
        dict_group = {}

        for i in strs:
            list_ = [0]*26
            for j in i:
                list_[alpha_dict[j]] += 1
            s = str(list_)
            if  s in dict_group:
                dict_group[s].append(i)
            else:
                dict_group[s] = [i]

        result = [] 
        # print(dict_group)
        for i in dict_group.keys():
                result.append(dict_group[i])

        return result
            
