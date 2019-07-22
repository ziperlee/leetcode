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
        return strs[0][:r.index(0)] if strs else ''

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
    assert s.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ''
    assert s.longestCommonPrefix(["abab","aba",""]) == ''