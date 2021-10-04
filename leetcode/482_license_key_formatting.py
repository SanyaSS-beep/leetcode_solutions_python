"""
@Description:
@Author: Mao Shuai Shuai
@Time: 2021/10/4 22:02
"""
import re


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cnt = 0
        ans = []
        for i in range(len(s)-1, -1, -1):
            if s[i] == '-':
                continue
            ans.append(s[i].upper())
            cnt = cnt + 1
            if cnt % k == 0:
                ans.append('-')
        if ans and ans[-1] == '-':
            ans.pop()
        return ''.join(ans[::-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.licenseKeyFormatting("2-5g-3-J", 2))
