class Solution:
    def non_rep(self,s):
        freq = {}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in s:
            if freq[ch] == 1:
                return ch
        return None
obj = Solution()
s= input()
print(obj.non_rep(s))