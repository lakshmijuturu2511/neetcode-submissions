class Solution:
    def isPalindrome(self, s: str) -> bool:
        result="".join(ch.lower() for ch in s if ch.isalnum())
        reverse=result[::-1]
        return result==reverse
            