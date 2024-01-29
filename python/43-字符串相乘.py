# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  示例 1:
#
#  输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#
#  输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#  说明：
#
#
#  num1 和 num2 的长度小于110。
#  num1 和 num2 只包含数字 0-9。
#  num1 和 num2 均不以零开头，除非是数字 0 本身。
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#  Related Topics 数学 字符串
#  👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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

# leetcode submit region end(Prohibit modification and deletion)
