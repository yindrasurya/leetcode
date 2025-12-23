class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        c = 0
        for ele in nums:
            while st and st[-1] > ele:
                st.pop()
            if ele == 0:
                continue
            if not st or st[-1] < ele:
                st.append(ele)
                c += 1
        return c