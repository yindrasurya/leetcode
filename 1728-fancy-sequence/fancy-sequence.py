class Fancy:
    
    def __init__(self):
        self.data = []
        self.cmul = [1]
        self.csum = [0]
        self.mod = 1_000_000_007

    def append(self, val: int) -> None:
        self.data.append(val)
        self.cmul.append(self.cmul[-1])
        self.csum.append(self.csum[-1])

    def addAll(self, inc: int) -> None:
        self.csum[-1] += inc

    def multAll(self, m: int) -> None:
        self.cmul[-1] = (self.cmul[-1] * m) % self.mod
        self.csum[-1] = (self.csum[-1] * m) % self.mod
        
    def getIndex(self, idx: int) -> int:
        if idx < len(self.data): 
            ratio = self.cmul[-1] * pow(self.cmul[idx], self.mod-2, self.mod) # Fermat's little theorem
            return ((self.data[idx] - self.csum[idx]) * ratio + self.csum[-1]) % self.mod
        return -1 

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)