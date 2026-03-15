class Fancy(object):

    def __init__(self):
        self.sequence = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7
    def append(self, val):
        self.sequence.append((val - self.add) * pow(self.mult, self.MOD-2, self.MOD) % self.MOD)
    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD
        
    def multAll(self, m):
        self.add = (self.add * m) % self.MOD
        self.mult = (self.mult * m) % self.MOD
        
    def getIndex(self, idx):
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.mult + self.add) % self.MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
