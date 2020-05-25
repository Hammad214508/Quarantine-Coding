"""
Given an array of integers and an integer k, you need to find the total
number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
"""
class Solution:

    # Helper funtion to add values into the hashMap or just increment its
    # value if it is already there
    def addToMap(self, elem, hashMap):
        if not elem in hashMap:
            hashMap[elem] = 1
        else:
            hashMap[elem] += 1
        return hashMap

    # Keep track of the sums we have seen so far and how many times we have
    # seen them in the a hashmap
    # Once we get a sum see if we have seen sum-k , if so then we have found
    # that many subarrays adding up to k
    def subarraySum(self, nums:[int], k: int) -> int:
        hashMap = {0:1}
        sum = 0
        result = 0
        for num in nums:
            sum += num
            if sum-k in hashMap.keys():
                result += hashMap[sum-k]
            hashMap = self.addToMap(sum, hashMap)
        return result



nums = [1,1,1]
k = 2

solution = Solution()
print(solution.subarraySum(nums, k))
