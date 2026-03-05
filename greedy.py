# 55. Jump Game (Medium)
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def canJump(self, nums):    
        last = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0

class Solution:
    def canJump(self, nums):
        farthest = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last:
                return True

        return True
    
# 435. Non-overlapping Intervals (Medium)
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals):#가장 빨리 끝나는거
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = intervals[0][1]
        for s, e in intervals[1:]:
            if s < prev_end:
                removed += 1
            else:
                prev_end = e

        return removed
# 253. Meeting Rooms II (Medium)
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        rooms = 0
        end_ptr = 0

        for s in starts:
            if s < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1

        return rooms

# 134. Gas Station (Medium)