class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i]+=1

        bucket = [[] for _ in range(len(nums)+1)]

        for i in freq_dict:
            print(freq_dict[i],bucket)
            bucket[freq_dict[i]].append(i)

        result = []

        for i in range(len(bucket)-1,0,-1):
            if bucket[i] != [] and k!=0:
                result.extend(bucket[i])
                k=k-len(bucket[i])
            


        # print(bucket)
        return result


        
        