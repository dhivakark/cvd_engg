import heapq


class MaxHeapObj(object):
  def __init__(self,val): 
    self.val = val
  def __lt__(self,other): 
    return self.val > other.val
  def __eq__(self,other): 
    return self.val == other.val
  def __str__(self):
    return str(self.val)

class MinHeap(object):
  def __init__(self): 
    self.h = []
  def heappush(self,x): 
    heapq.heappush(self.h,x)
  def heappop(self): 
    return heapq.heappop(self.h)
  def __getitem__(self,i): 
    return self.h[i]
  def __len__(self): 
    return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): 
    heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): 
    return heapq.heappop(self.h).val
  def __getitem__(self,i): 
    return self.h[i].val
  
def main():
  n = int(raw_input().strip())
  a = []
  a_i = 0
  max_heap = MaxHeap()
  min_heap = MinHeap()
  for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    max_heap.heappush(a_t)
    if len(max_heap) - len(min_heap) >= 2:
      print 'length', len(max_heap), len(min_heap)
      largest_element = max_heap.heappop() 
      min_heap.heappush(largest_element)
    if len(max_heap) > 0 and len(min_heap) > 0:
      if max_heap[0] > min_heap[0]:
        max_heap0 = max_heap.heappop()
        min_heap0 = min_heap.heappop()
        max_heap.heappush(min_heap0)
        min_heap.heappush(max_heap0)

    if (len(max_heap) + len(min_heap)) % 2 == 0:
      print (max_heap[0] + min_heap[0]) / 2.0
    else:
      print max_heap[0]

if __name__ == '__main__':
  main()
