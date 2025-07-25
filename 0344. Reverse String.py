# Approach 01

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l , r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
          

# Approach 02

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l , r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1


