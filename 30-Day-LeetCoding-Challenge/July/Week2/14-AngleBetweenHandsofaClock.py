"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between
the hour and the minute hand.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5

Example 4:
Input: hour = 4, minutes = 50
Output: 155

Example 5:
Input: hour = 12, minutes = 0
Output: 0

Constraints:
    1 <= hour <= 12
    0 <= minutes <= 59
    Answers within 10^-5 of the actual value will be accepted as correct.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        if (hour == 12):
            hour = 0
        if (minutes == 60):
            minutes = 0
            hour += 1;
            if(hour>12):
                   hour = hour-12;

        # Calculate the angles moved by
        # hour and minute hands with
        # reference to 12:00
        hour_angle = 0.5 * (hour * 60 + minutes)
        minutes_angle = 6 * minutes

        # Find the difference between two angles
        angle = abs(hour_angle - minutes_angle)

        # Return the smaller angle of two
        # possible angles
        angle = min(360 - angle, angle)

        return angle
