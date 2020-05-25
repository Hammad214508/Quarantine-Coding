"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has
new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone
(or 0 if there are no stones left.)



Example 1:
Input: [2,7,4,1,8,1]
Output: 1

Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""

# O(n log n)
def lastStoneWeight(stones: [int]) -> int:
    # While there are stones
    while len(stones) > 1:
        # Sort in descending order
        stones.sort(reverse=True)
        # The the top 2 are equal delete both
        if stones[0] == stones[1]:
            # Both zero as the list shifts when one is deleted
            del stones[0]
            del stones[0]
        else:
            # Otherwise the larget one is reduces by the smaller one
            stones[0] -= stones[1]
            # The smaller one is deleted
            del stones[1]
    # If there is a stone then return the weight
    if stones:
        return stones[0]
    # Otherwise it's 0
    else:
        return 0
