class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a, b = num1[::-1], num2[::-1]
        res = 0

        for i, n1 in enumerate(a):
            res_j = 0
            for j, n2 in enumerate(b):
                res_j += self.str2int(n1) * self.str2int(n2) * 10 ** j
            res += res_j * 10 ** i
        return str(res)

    def str2int(self, s):
        return ord(s) - ord("0")


def test():
    s = Solution()
    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"
