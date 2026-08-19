class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=[]
        p1=0
        p2=n
        for i in range(n):
            arr.append(nums[p1])
            arr.append(nums[p2])
            p1+=1
            p2+=1
        return arr
