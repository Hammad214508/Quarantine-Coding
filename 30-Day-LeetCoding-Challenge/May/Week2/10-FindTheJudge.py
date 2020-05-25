"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people
is secretly the town judge.

If the town judge exists, then:
    - The town judge trusts nobody.
    - Everybody (except for the town judge) trusts the town judge.
    - There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled
a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""

class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        if len(trust) == 1:
            return trust[0][1]
        hash = {i:set() for i in range(1, N+1)}
        for t in trust:
            hash[t[0]].add(t[1])
        for i in range(1, N+1):
            if not hash[i]:
                trust_count = 0
                for key, value in hash.items():
                    if i in value:
                        trust_count += 1
                if trust_count == N-1:
                    return i
        return -1

    def findJudge(self, N, trust):
        trusts = [0] * (N+1)
        for (a, b) in trust:
            trusts[a] -= 1
            trusts[b] += 1
        for i in range(1, len(trusts)):
            if trusts[i] == N-1:
                return i
        return -1

solution = Solution()
N = 3
trust = [[1,3],[2,3]]
res = solution.findJudge(N, trust)
print(res)
