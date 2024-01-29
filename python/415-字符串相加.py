
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#
#
#  提示：
#
#
#  num1 和num2 的长度都小于 5100
#  num1 和num2 都只包含数字 0-9
#  num1 和num2 都不包含任何前导零
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
#
#  Related Topics 字符串
#  👍 381 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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
# leetcode submit region end(Prohibit modification and deletion)
