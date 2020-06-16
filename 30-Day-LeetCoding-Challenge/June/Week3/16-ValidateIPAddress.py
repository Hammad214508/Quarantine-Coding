"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers,
each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits.
The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one.
Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to
upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive
colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334
is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
    Input: "172.16.254.1"
    Output: "IPv4"
    Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
    Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
    Output: "IPv6"
    Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
    Input: "256.256.256.256"
    Output: "Neither"
    Explanation: This is neither a IPv4 address nor a IPv6 address.
"""
class Solution:

    def checkIPv4(self, IP):
        IP = IP.split(".")
        # 4 decimal numbers
        if len(IP) != 4:
            return False
        # For each number
        for num in IP:
            # Check is a number
            if not num.isdigit():
                return False
            # No leading zeros
            if len(num) != len(str(int(num))):
                return False
            # Between 0 and 255
            if int(num) < 0 or int(num) > 255:
                return False
        return True

    def isHex(self, num):
        validHexChar = {'A', 'B', 'C', 'D', 'E', 'F'}
        for n in range(10):
            validHexChar.add(str(n))
        for digit in num:
            if not (digit.upper() in validHexChar):
                return False
        return True

    def checkIPv6(self, IP):
        IP = IP.split(":")
        # 8 groups of four hexadecimal digits
        if len(IP) != 8:
            return False
        # For each figit
        for num in IP:
            # Can't be empty or more than 4 digits
            if len(num) == 0 or len(num) > 4:
                return False
            # Check is hex
            if not self.isHex(num):
                return False
        return True

    def validIPAddress(self, IP: str) -> str:
        isIPv4 = self.checkIPv4(IP)
        if isIPv4:
            return "IPv4"

        isIPv6 = self.checkIPv6(IP)
        if isIPv6:
            return "IPv6"

        return "Neither"

solution = Solution()
ip1 = "172.16.254.1"
ip2 = "2001:0db8:85a3:0:0:8A2E:0370:7334"
ip3 = "256.256.256.256"
res = solution.validIPAddress(ip2)
print(res)
