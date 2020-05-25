"""
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.
"""

# O(n^2)
# Goes through each element and checks if elem+! is in the list
# if so then increment a counter
def countElements0(arr:[int]) -> int:
    count = 0
    for elem in arr:
        # Check if elem + 1 is there
        if elem+1 in arr:
            count+=1
    return count

# O(n)
# Puts all the elements in a hashmap and for each element
# check if elem + 1 is in the hash (this takes now O(1)) and
# increment counter
def countElements(arr:[int]) -> int:
    count = 0
    hash = set()
    for elem in arr:
        hash.add(elem)
    for elem in arr:
        # Check if elem + 1 is there
        if elem+1 in hash:
            count+= 1
    return count
