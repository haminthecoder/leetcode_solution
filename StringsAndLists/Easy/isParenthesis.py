class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
if __name__ == "__main__":
    s = Solution()
    s.isValid('{hel}')
    