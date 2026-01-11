class Solution:
    def remove_dup(self,s):
        result = " "
        for ch in s:
            if ch not in result:
                result += ch
        return result
    
obj = Solution()
s = input()
print(obj.remove_dup(s))

