class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or not 1 <= urgency <= 10:
            raise ValueError("urgency must be an integer from 1 to 10.")
        self.name = name
        self.urgency = urgency


class MinHeap:
   def __init__(self):
        self.data = []
 
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break
 
    def heapify_down(self, index):
        n = len(self.data)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < n and self.data[left].urgency < self.data[smallest].
                smallest = left
            if right < n and self.data[right].urgency < self.data[smallest]:
                smallest = right
            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

if __name__ == "__main__":
    heap = MinHeap()
    assert heap.peek() is None and heap.remove_min() is None
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    nxt = heap.peek()
    print(nxt.name, nxt.urgency)
    assert heap.remove_min().name == "Taylor"
    heap.print_heap()
    assert [heap.remove_min().name for _ in range(2)] == ["Jordan", "Avery"]
    try:
        Patient("Bad", 11)
    except ValueError as e:
        print("OK:", e)# Test your MinHeap class here including edge cases
