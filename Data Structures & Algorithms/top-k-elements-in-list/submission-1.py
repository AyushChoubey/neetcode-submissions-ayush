class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for i in range(len(nums)+1)]
        freq_dict = {}
        result = []
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i]+=1
        max_freq = 0
        print(freq_dict,bucket)
        for i in freq_dict:
            if freq_dict[i] >max_freq:
                max_freq = freq_dict[i] 
            bucket[freq_dict[i] ].append(i)

        print(bucket)
        for i in range(max_freq, 0,-1):
            if len(result)==k:
                break
            if len(bucket[i])>=k:
                result.extend(bucket[i][:k])
                break
            else:
                if len(result) <k:
                    result.extend(bucket[i])
                else:
                    break
        return result 



        



            

        
        