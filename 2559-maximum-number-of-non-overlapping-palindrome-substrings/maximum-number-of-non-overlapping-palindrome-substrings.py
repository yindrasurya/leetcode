class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        last_end = 0

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for right in range(k - 1, n):
            left = right - k + 1

            add = (
                (left >= last_end and is_palindrome(left, right)) or
                (left > last_end and is_palindrome(left - 1, right))
            )

            if add:
                count += 1
                last_end = right + 1

        return count