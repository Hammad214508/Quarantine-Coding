"""
Given a list of airline tickets represented by pairs of departure and arrival airports
[from, to], reconstruct the itinerary in order. All of the tickets belong to a man who
departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest
lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"]
has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:
    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation:
        Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
        But it is larger in lexical order.
"""
from collections import defaultdict

class Solution:
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

    def findItinerary(self, tickets):
        self.route = []
        self.adj_list = defaultdict(list)
        for i,j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list:
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)

        self.dfs("JFK")
        return self.route[::-1]

solution = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
res = solution.findItinerary(tickets)
print(res)
