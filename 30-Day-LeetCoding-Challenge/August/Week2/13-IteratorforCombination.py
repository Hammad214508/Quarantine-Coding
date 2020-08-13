"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.comb = [i for i in range(combinationLength-1)] + [combinationLength-2]

    def next(self) -> str:
        for i in range(1, len(self.comb)+1):
            if self.comb[-i] < len(self.s)-i:
                self.comb[-i] += 1
                while i != 1:
                    self.comb[-i+1] = self.comb[-i] + 1
                    i -= 1
                break

        return ''.join([self.s[pos] for pos in self.comb])

    def hasNext(self) -> bool:
        return self.comb[0] != len(self.s) - len(self.comb)
