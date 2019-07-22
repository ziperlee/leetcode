class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        length = len(num1) if len(num1) < len(num2) else len(num2)
        revs_num1 = num1[-1::-1]
        revs_num2 = num2[-1::-1]
        p, tmp = 0, 0
        while p < length:
            n1 = ord(revs_num1[p]) - ord('0')
            n2 = ord(revs_num2[p]) - ord('0')
            res.append(str((n1+n2)%10 + tmp))
            tmp = (n1+n2)//10
            p += 1
        nums = revs_num1 if len(num1) > len(num2) else revs_num2
        tmp += nums[-1]
        res.extend(nums[p:])
        res.reverse()
        return ''.join(res)

def test():
    s = Solution()
    assert s.addStrings('100', '100') == '200'
    assert s.addStrings('123',  '234') == '357'
    assert s.addStrings('123', '2340') == '2463'
    assert s.addStrings('1', '9') == '10'