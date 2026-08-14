class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        start = 0

        storage = {}

        for end in range(len(s)):
            storage[s[end]] = storage.get(s[end], 0) + 1
            while storage[s[end]] > 2:
                storage[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)

        return result