class SmallestInfiniteSet:
    def __init__(self):
        self.present = [True] * 1001
        self.current = 1

    def popSmallest(self) -> int:
        val = self.current
        self.present[val] = False
        while self.current < len(self.present) and not self.present[self.current]:
            self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if not self.present[num]:
            self.present[num] = True
            if num < self.current:
                self.current = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)