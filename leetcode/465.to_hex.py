"""
@Description:
@Author: Mao Shuai Shuai
@Time: 2021/10/4 18:22
"""
class Solution:
    def toHex(self, num: int) -> str:
        hex_gr_10 = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g'}
        hex_str = ''
        for _ in range(8):
            mod = num % 16
            num = num // 16
            if not num:
                break
            if mod > 9:
                hex_str = hex_gr_10[mod] + hex_str
            else:
                hex_str = str(mod) + hex_str
        return hex_str
