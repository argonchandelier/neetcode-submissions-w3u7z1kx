class KthLargest:
    def heapify_down(self, i):
        sm = i
        l = 2*i + 1
        r = 2*i + 2

        if l < len(self.heap) and self.heap[l] < self.heap[sm]:
            sm = l
        if r < len(self.heap) and self.heap[r] < self.heap[sm]:
            sm = r
        
        if sm != i:
            self.heap[i], self.heap[sm] = self.heap[sm], self.heap[i]
            self.heapify_down(sm)
    
    def insert(self, value):
        if len(self.heap) < self.k:
            self.heap.append(value)  # Add to heap
            self.heapify_up(len(self.heap) - 1)  # Restore heap property
        elif value > self.heap[0]:  # If value > min element, replace it
            self.heap[0] = value  # Replace root
            self.heapify_down(0)  # Restore heap property

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:  # Min-Heap property
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)  # Recursively fix heap

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.n = len(nums)
        self.k = k

        for num in nums:
            self.insert(num)
        
        print(f"first: {self.heap}")

    def add(self, val: int) -> int:
        #print(self.nums)
        self.insert(val)
        print(self.heap)

        return self.heap[0]
        
