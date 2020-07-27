class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = (ord(num1[i]) - ord("0")) if i >= 0 else 0
            n2 = (ord(num2[j]) - ord("0")) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res.append(str(tmp % 10))
            i, j = i - 1, j - 1
        if carry:
            res.append(str(carry))
        # res.reverse()
        return "".join(res[::-1])


def test():
    s = Solution()
    assert s.addStrings("100", "100") == "200"
    assert s.addStrings("123", "234") == "357"
    assert s.addStrings("123", "2340") == "2463"
    assert s.addStrings("1", "9") == "10"
    assert s.addStrings("9", "99") == "108"
