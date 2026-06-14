class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i].priority > self.heap[parent].priority:
            self._swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# TESTING PART (FOR SCREENSHOT)
pq = PriorityQueue()
pq.insert(Task("A", 10))
pq.insert(Task("B", 5))
pq.insert(Task("C", 20))

print("Max Task:", pq.extract_max().task_id)