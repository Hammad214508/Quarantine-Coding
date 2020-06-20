"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""
import itertools
from math import factorial

class Solution:
    def getPermutation0(self, n: int, k: int) -> str:
        lst = [x for x in range(1, n+1)]
        perm = list(itertools.permutations(lst))
        kth = perm[k-1]
        res = ""
        for num in kth:
            res += str(num)
        return res
    
    # Let us consider an example: n=6, k=314. How we can find the first digit?
    # There are 5! = 120 permutations, which start with 1, there are also 120 permutations,
    # which start with 2, and so on. 314 > 2*120 and 314 < 3*120, so it means, that the fist digit
    # we need to take is 3. So we build first digit of our number, remove it from list of all digits digits and continue:
    #
    # k = 314-2*5! = 74, n - 1 = 5, d = 3, build number so far 3, digits = [1,2,4,5,6]
    # k = 74-3*4! = 2, n - 1 = 4, d = 0, build number so far 35, digits = [1,2,4,6]
    # k = 2-0*3! = 2, n - 1 = 3, d = 0, build number so far 351, digits = [2,4,6]
    # k = 2-1*2! = 0, n - 1 = 2, d = 2, build number so far 3512, digits = [4,6]
    # k = 0-1*1! = 0, n - 1 = 1, d = 2, build number so far 35126, digits = [4]
    # Finally, we have only one digit left, output is 351264.
    #
    # Complexity. I keep list of n digits, and then delete them one by one.
    # Complexity of one deletion is O(n), so overall complexity is O(n^2).
    # Note, that it can be improved to O(n log n) if we use SortedList, but it just not worth it, n is too small.
    def getPermutation(self, n, k):
        numbers = list(range(1,n+1))
        answer = ""

        for n_it in range(n,0,-1):
            d = (k-1)//factorial(n_it-1)
            k -= d*factorial(n_it-1)
            answer += str(numbers[d])
            numbers.remove(numbers[d])

        return answer

solution  = Solution()
n = 3
k = 3
res = solution.getPermutation(n, k)
print(res)
