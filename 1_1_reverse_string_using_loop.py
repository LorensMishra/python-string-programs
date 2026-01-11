class Solution:
    def reverse_string_loop(self,s):
        if len(s) == 0:
            return " "
        res=" "
        for ch in s:
            res = ch + res
        return res
obj = Solution()
s = input()
print(obj.reverse_string_loop(s))    