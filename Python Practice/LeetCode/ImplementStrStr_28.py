class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            i = 0   #index of haystack
            j = 0   #index of needle

            while i < len(haystack):
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    i = i - j + 1
                    j = 0
                if j == len(needle):
                    return i - j
            return -1