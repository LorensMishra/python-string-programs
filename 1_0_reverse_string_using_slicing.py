# create a class name Solution
class Solution:
    # reverse of a string
    def reverse_using_slicing(self,s):
        return s[::-1]
s = input("Enter a string:")
obj = Solution()
print(obj.reverse_using_slicing(s))