"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_list = sorted(intervals, key=lambda x: x.start)

        bound = -1
        

        for i in sorted_list:
            if i.start>= bound:
                bound = i.end
            else:
                return False
        return True
            
            
