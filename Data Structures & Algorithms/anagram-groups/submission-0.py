class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        dict_str = {}
        result = []
        for i in strs:
            sorted_characters = sorted(i)

            new_str = "".join(sorted_characters)
            if new_str in dict_str:
                dict_str[new_str].append(i)
            else:
                dict_str[new_str] = [i]

        for i in dict_str.keys():
            result.append(dict_str[i])

        return result

        
    