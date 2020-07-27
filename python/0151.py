class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])


def test():
    s = Solution()
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world!  ") == "world! hello"
    assert s.reverseWords("a good   example") == "example good a"
