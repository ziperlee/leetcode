# 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#
#
#  示例 1：
#
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#
#
#  示例 2：
#
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
#
#  提示：
#
#
#  0 <= strs.length <= 200
#  0 <= strs[i].length <= 200
#  strs[i] 仅由小写英文字母组成
#
#  Related Topics 字符串
#  👍 1643 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if len(strs) == 0:
        #     return ''
        # res = strs[0]
        # for s in strs[1:]:
        #     len_res, len_s = len(res), len(s)
        #     length = len_res if len_res < len_s else len_s
        #     if length == 0:
        #         res = ''
        #         break
        #     for idx, _s in enumerate(s[:length]):
        #         if res[idx] != _s:
        #             idx -= 1
        #             break
        #     res = res[:idx+1]
        # return res

        # zip 提取相同位置的字符，set判断是否为公共字符，index查询第一个未匹配字符位置
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][: r.index(0)] if strs else ""

        # res = ""
        # for tmp in zip(*strs):
        #     tmp_set = set(tmp)
        #     if len(tmp_set) == 1:
        #         res += tmp[0]
        #     else:
        #         break
        # return res


def test():
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["abab", "aba", ""]) == ""
# leetcode submit region end(Prohibit modification and deletion)
