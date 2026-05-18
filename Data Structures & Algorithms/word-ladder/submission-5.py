from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        if endWord not in wordList:
            return 0
        
        q = deque([beginWord])
        
        graph = {}
        def differs_by_one(w1, w2):
            if len(w1) != len(w2):
                return False
            
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
                if diff > 1:        # early exit!
                    return False
            
            return diff == 1

        

        
        cnt=1
        visited = set()
        wordset = set(wordList)
        while q:

            for _ in range(len(q)):
                w1 = q.popleft()  
                
                visited.add(w1)
                if w1 == endWord:
                    return cnt

                for i in range(len(w1)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        w2 = w1[:i]+c+w1[i+1:]
                        if w2 in wordset and w2 not in visited:
                            visited.add(w1)
                            q.append(w2)
                
                # print(q)
                # if not q:
                #     return 0

            cnt+=1

        return 0
        
        




        
        