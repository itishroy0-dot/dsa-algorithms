class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*(2*self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n+i] = arr[i]
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]

    def query(self, l, r):
        res = 0
        l += self.n; r += self.n
        while l < r:
            if l%2:
                res += self.tree[l]; l += 1
            if r%2:
                r -= 1; res += self.tree[r]
            l//=2; r//=2
        return res

# Example
arr = [1,2,3,4,5]
seg = SegmentTree(arr)
print(seg.query(1,4))  # sum from index 1 to 3 → 9
seg.update(2,10)
print(seg.query(1,4))  # updated sum → 16
