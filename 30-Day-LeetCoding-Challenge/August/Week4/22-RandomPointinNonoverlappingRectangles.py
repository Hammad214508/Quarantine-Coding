"""
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:
    An integer point is a point that has integer coordinates.
    A point on the perimeter of a rectangle is included in the space covered by the rectangles.
    ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
    length and width of each rectangle does not exceed 2000.
    1 <= rects.length <= 100
    pick return a point as an array of integer coordinates [p_x, p_y]
    pick is called at most 10000 times.

Example 1:
    Input:
    ["Solution","pick","pick","pick"]
    [[[[1,1,5,5]]],[],[],[]]
    Output:
    [null,[4,1],[4,1],[3,3]]

Example 2:
    Input:
    ["Solution","pick","pick","pick","pick","pick"]
    [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
    Output:
    [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
    Explanation of Input Syntax:

    The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""

from random import randint

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rect_rngs = []
        range_start = 0
        for x1,y1,x2,y2 in rects:
            num_points_in_rect = (x2-x1+1) * (y2-y1+1)
            self.rect_rngs.append([[range_start,range_start+num_points_in_rect], [x1,y1,x2,y2]])
            range_start = range_start+num_points_in_rect
        self.total_points = range_start
    def pick(self) -> List[int]:
        def pick_rectangle():
            rnd_int = randint(0,self.total_points-1)
            for rng, rect in self.rect_rngs:
                if rng[0]<=rnd_int<rng[1]:
                    return rect
            raise ValueError("No matching rectangle found!")
        x1,y1,x2,y2 = pick_rectangle()
        pick_x = randint(x1,x2) # randint(a,b) is inclusive!
        pick_y = randint(y1,y2)
        return [pick_x, pick_y]
