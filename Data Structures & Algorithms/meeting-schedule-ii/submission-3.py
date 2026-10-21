"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start  = []
        end = []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)


        start = sorted(start)
        end = sorted(end)

        s = 0
        e = 0
        max_count = 0
        count =0

        while s< len(start):

            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            
            max_count = max(max_count,count)

        return max_count



