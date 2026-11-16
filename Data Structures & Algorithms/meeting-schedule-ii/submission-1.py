"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        count_rooms = 0
        rooms_needed = 0
        #want to interate throughthe earlierest start times
        while s < len(start):
            #if the easilesrt start time of a meeting less then earliest end time a meeting we know that there is an overlap in meeting times
            if start[s] < end[e]:
                count_rooms += 1
                rooms_needed = max(rooms_needed, count_rooms)
                s += 1
            #other case, when 
            else:
                count_rooms -= 1
                e += 1
        return rooms_needed


