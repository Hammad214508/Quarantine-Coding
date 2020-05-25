"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue,
 and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:
Input:
    ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add",
    "showFirstUnique"]
    [[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
    [null,2,null,2,null,3,null,-1]

Explanation:
    FirstUnique firstUnique = new FirstUnique([2,3,5]);
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(5);            // the queue is now [2,3,5,5]
    firstUnique.showFirstUnique(); // return 2
    firstUnique.add(2);            // the queue is now [2,3,5,5,2]
    firstUnique.showFirstUnique(); // return 3
    firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
    firstUnique.showFirstUnique(); // return -1

Example 2:
Input:
    ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
    [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
    [null,-1,null,null,null,null,null,17]
Explanation:
    FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
    firstUnique.showFirstUnique(); // return -1
    firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
    firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
    firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
    firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
    firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
    firstUnique.showFirstUnique(); // return 17

Example 3:
Input:
    ["FirstUnique","showFirstUnique","add","showFirstUnique"]
    [[[809]],[],[809],[]]
Output:
    [null,809,null,-1]
Explanation:
    FirstUnique firstUnique = new FirstUnique([809]);
    firstUnique.showFirstUnique(); // return 809
    firstUnique.add(809);          // the queue is now [809,809]
    firstUnique.showFirstUnique(); // return -1
"""

class FirstUnique:

    def __init__(self, nums:[int]):
        # Initialise queue and hash and add the first elemets
        self.queue = []
        self.hash = {} #Keeps a counter of how many time a value appeared
        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        # Remove all the elements from the head of the queue if they appear more than once
        while len(self.queue) > 0 and self.hash[self.queue[0]] > 1:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        # Return the head of the queue now having the first unique value
        else:
            return self.queue[0]


    def add(self, value: int) -> None:
        # If the value is already in the hash then increment it's occurences
        if value in self.hash:
            self.hash[value] += 1
        # Otherwise, add it in the hash and in the queue (queue only has unique ones)
        else:
            self.hash[value] = 1
            self.queue.append(value)




nums = [2,3,5]
obj = FirstUnique(nums)
print(obj.showFirstUnique())
obj.add(5)
print(obj.showFirstUnique())
obj.add(2);
print(obj.showFirstUnique())
obj.add(3);
print(obj.showFirstUnique())
