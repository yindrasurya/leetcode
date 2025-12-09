class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        n = len(fruits)
        cnt = defaultdict(int)
        i = 0
        ans = 0
        for j, f in enumerate(fruits):
            cnt[f] += 1
            while len(cnt) > 2:
                cnt[fruits[i]] -= 1
                if cnt[fruits[i]] == 0:
                    del cnt[fruits[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans