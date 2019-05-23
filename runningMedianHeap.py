
class MinHeap(object):
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        len_heap = len(self.heap)
        for i in xrange(len_heap//2, -1, -1):
            self.__min_heapify(i, len_heap)

    def __min_heapify(self, root, len_heap):
        left = 2 * root + 1
        right = 2 * root + 2
        smallest = root
        if left <= len_heap-1 and self.heap[left] < self.heap[root]:
            smallest = left
        if right <= len_heap-1 and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != root:
            self.heap[root], self.heap[smallest] = self.heap[smallest], self.heap[root]
            self.__min_heapify(smallest, len_heap)

    def remove(self):
        x = self.heap.pop(0)
        len_heap = len(self.heap)
        for i in xrange(len_heap//2, -1, -1):
            self.__min_heapify(i, len_heap)
        return x

    def getMin(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def printHeap(self):
        return self.heap


class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        len_heap = len(self.heap)
        for i in xrange(len_heap//2, -1, -1):
            self.__max_heapify(i, len_heap)

    def __max_heapify(self, root, len_heap):
        left = 2 * root + 1
        right = 2 * root + 2
        largest = root
        if left <= len_heap-1 and self.heap[left] > self.heap[root]:
            largest = left
        if right <= len_heap-1 and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != root:
            self.heap[root], self.heap[largest] = self.heap[largest], self.heap[root]
            self.__max_heapify(largest, len_heap)

    def remove(self):
        x = self.heap.pop(0)
        len_heap = len(self.heap)
        for i in xrange(len_heap//2, -1, -1):
            self.__max_heapify(i, len_heap)
        return x

    def getMax(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def printHeap(self):
        return self.heap


def runningMedian(inp):
    effectiveMedian = 0
    minH = MinHeap()
    maxH = MaxHeap()
    for i in inp:
        if i > effectiveMedian:
            minH.insert(i)
        else:
            maxH.insert(i)
        # re balance the heaps
        lenMinHeap = len(minH)
        lenMaxHeap = len(maxH)
        if abs(lenMinHeap-lenMaxHeap) > 1:
            if lenMinHeap > lenMaxHeap:
                maxH.insert(minH.remove())
            else:
                minH.insert(maxH.remove())

        lenMinHeap = len(minH)
        lenMaxHeap = len(maxH)
        if lenMinHeap == lenMaxHeap:
            effectiveMedian = (minH.getMin() + maxH.getMax()) / 2.0
        elif lenMinHeap > lenMaxHeap:
            effectiveMedian = minH.getMin()
        else:
            effectiveMedian = maxH.getMax()
        print effectiveMedian


if __name__ == '__main__':
    inp = [6, 12, 4, 5, 3, 8, 7]
    inp = [5, 15, 10, 20, 3]
    runningMedian(inp)
