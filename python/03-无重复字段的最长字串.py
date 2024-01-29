"""
 Create by zipee on 2019/7/2.
"""
__author__ = "zipee"


# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
#  示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#  示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 104
#  s 由英文字母、数字、符号和空格组成
#
#  Related Topics 哈希表 双指针 字符串 Sliding Window
#  👍 5616 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max_len = 0
        cur_s = []
        for _s in s:
            if _s in cur_s:
                idx = cur_s.index(_s)
                if len(cur_s) > max_len:
                    max_len = len(cur_s)
                cur_s = cur_s[idx + 1:]
            cur_s.append(_s)

        if len(cur_s) > max_len:
            max_len = len(cur_s)

        return max_len


def test():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("aabaab!bb") == 3
# leetcode submit region end(Prohibit modification and deletion)
