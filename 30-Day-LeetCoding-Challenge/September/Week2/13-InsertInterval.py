"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]

Example 4:
    Input: intervals = [[1,5]], newInterval = [2,3]
    Output: [[1,5]]

Example 5:
    Input: intervals = [[1,5]], newInterval = [2,7]
    Output: [[1,7]]

Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= intervals[i][0] <= intervals[i][1] <= 105
    intervals is sorted by intervals[i][0] in ascending order.
    newInterval.length == 2
    0 <= newInterval[0] <= newInterval[1] <= 105
"""

class Solution:
    def insert(self, intervals: List[List[int]], n_itl: List[int]) -> List[List[int]]:
        if not intervals:
            return [n_itl]
        for i in range(len(intervals)):
            # position found and check will it overlap?
            if intervals[i][1] >= n_itl[0]:
                for j in range(i,len(intervals)):
                    # first not overlap
                    if n_itl[1] < intervals[j][0]:
                        # no overlap
                        if j == i:
                            intervals.insert(i,n_itl)
                            return intervals
                        return intervals[:i] + [[min(intervals[i][0], n_itl[0]), max(intervals[j-1][1], n_itl[1]) ]] + intervals[j:]
                # overlap with all remaining
                return intervals[:i]+[[min(intervals[i][0],n_itl[0]),max(n_itl[1],intervals[j][1])]]
        # not overlap and greater than all intervals
        return intervals+[n_itl]
