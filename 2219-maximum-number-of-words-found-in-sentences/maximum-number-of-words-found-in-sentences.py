class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        max_words = 0
        for sentence in s:
            cnt = len(sentence.split(" "))
            max_words = max(max_words, cnt)
        return max_words  