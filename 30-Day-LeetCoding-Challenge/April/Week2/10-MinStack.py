"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        self.min = float('inf') # Set the initial minimum to infinity
        self.stack = [] # Stack represented as a list

    def push(self, x: int) -> None:
        # If the new value if less than the current minimum
        # push the minimum value to the stack, update the variable min and
        # push the value x into the stack
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        # Get the top of the stack
        t = self.stack.pop()
        # If the top of the stack was also the minimum value need to update the minimum value and then
        # pop the stack again
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        # Return the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the minimum value
        return self.min
