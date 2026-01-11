class LongestCommonPrefix:
    def lcp(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix


# Runtime input
obj = LongestCommonPrefix()
n = int(input("Enter number of strings: "))
arr = [input() for _ in range(n)]


print("Longest Common Prefix:", obj.lcp(arr))
