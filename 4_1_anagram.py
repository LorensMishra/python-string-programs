class Solution:
    def check_ana(self,s1,s2):
        if len(s1)!=len(s2):
            return None
        freq = {}
        for ch in s1:
            freq[ch]=freq.get(ch,0)+1
        for ch in s2:
            if ch not in freq or freq[ch]==0:
                return False
            freq[ch]-=1
        return True
obj = Solution()
s1 = input()
s2 = input()
print(obj.check_ana(s1,s2))
            