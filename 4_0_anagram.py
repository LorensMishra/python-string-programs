class Solution:
    def check_ana(self,s1,s2):
        if len(s1)!=len(s2):
            return None
        return sorted(s1)==sorted(s2)
obj = Solution()
s1 = input()
s2 = input()
print(obj.check_ana(s1,s2))