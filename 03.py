"""
 Create by zipee on 2019/7/2.
"""
__author__ = 'zipee'


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
                cur_s = cur_s[idx+1:]
            cur_s.append(_s)

        if len(cur_s) > max_len:
            max_len = len(cur_s)

        return max_len


def test():
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring('aabaab!bb') == 3
