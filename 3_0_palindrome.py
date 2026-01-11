class Solution:
    def check_palindrome(self,s):
        return s==s[::-1]
s = input()
obj = Solution()
if obj.check_palindrome(s):
    print("palindrome")
else:
    print("no")