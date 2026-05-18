class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        if endWord not in wordList:
            return 0

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

        

        q = []
        q.append(beginWord)
        cnt=0
        visited = set()
        while q:

            for _ in range(len(q)):
                w1 = q.pop(0)
                visited.add(w1)
                if w1 == endWord:
                    return cnt+1
                for w2 in wordList:
                    if w2 not in visited:
                        if differs_by_one(w1,w2):
                            q.append(w2)
                # print(q)
                if not q:
                    return 0

            cnt+=1
        
        




        
        