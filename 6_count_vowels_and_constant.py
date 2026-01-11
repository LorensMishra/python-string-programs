class Solution:
    def count_a_v(self,s):
        vowels = "aeiouAEIOU"
        v = c = 0
        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    v+=1
                else:
                    c+=1

        return v,c
obj = Solution()
s = input()
print(obj.count_a_v(s))
