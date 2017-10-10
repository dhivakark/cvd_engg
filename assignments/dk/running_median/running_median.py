''' Binary Heap Implementation '''

import math

class Heap(object):
  '''
  Binary Heap class implementation
  '''
  def __init__(self, max_heap=False):
    '''
    Construct the elements of the Binary heap
    '''
    self.elems = [0]
    self.max_heap = max_heap
    self.level = 0

  @property
  def size(self):
    return len(self.elems) - 1

  @property
  def max_elem(self):
    return self.elems[1]

  @property
  def min_elem(self):
    return self.elems[1]

  def insert(self, elem):
    '''
    Insert the element 'elem' to the heap
    '''
    self.elems.append(elem)
    self.level = int(math.floor(math.log2(len(self.elems[1:])))) + 1
    self.percolate_up()

  def display(self):
    '''
    Display the Binary heap
    '''
    # Print it in the order
    # TODO: Find a way to print it in the tree form
    idx = 1
    for r in range(self.level):
      elems = [str(self.elems[idx + c]) for c in range(2 ** r)
              if idx + c <= len(self.elems[1: ])]
      idx += 2 ** r
      print('  '.join(elems))

  def percolate_up(self):
    '''
    Percolate the heap from the last element to first
    '''
    elem = self.elems[-1]
    elem_idx = len(self.elems[1:])
    for itr in range(self.level - 1):
      parent_idx = elem_idx // 2
      parent = self.elems[parent_idx]
      if (elem > parent) != self.max_heap:
        break

      # Swap the parent and child elements
      self.elems[elem_idx], self.elems[parent_idx] = parent, elem
      elem_idx = elem_idx // 2

  def percolate_down(self):
    '''
    Percolate the heap from the last element to first
    '''
    elem = self.elems[1]
    elem_idx = 1
    for itr in range(self.level - 1):
      child1_idx = elem_idx * 2
      if child1_idx >= len(self.elems):
        break
      child1 = self.elems[child1_idx]

      child2_idx = elem_idx * 2 + 1
      if child2_idx < len(self.elems):
        child2 = self.elems[child2_idx]
        if child1 > child2:
          child = child1 if self.max_heap else child2
          child_idx = child1_idx if self.max_heap else child2_idx
        else:
          child = child2 if self.max_heap else child1
          child_idx = child2_idx if self.max_heap else child1_idx
      else:
        child, child_idx = child1, child1_idx

      if (child > elem) != self.max_heap:
        break

      # Swap the parent and child elements
      self.elems[elem_idx], self.elems[child_idx] = child, elem
      elem_idx = child_idx


  def delete_min(self):
    '''
    Delete the minimum element in the Heap
    '''
    if self.max_heap:
      print('You cannot delete Minimum from Max Heap')
      return None

    if len(self.elems[1:]) == 1:
      return self.elems.pop()

    min_num = self.elems[1]
    self.elems[1] = self.elems.pop()
    self.level = int(math.floor(math.log2(len(self.elems[1:])))) + 1
    self.percolate_down()
    return min_num

  def delete_max(self):
    '''
    Delete the minimum element in the Heap
    '''
    if not self.max_heap:
      print('You cannot delete Maximum from Min Heap')
      return None

    if len(self.elems[1:]) == 1:
      return self.elems.pop()

    max_num = self.elems[1]
    self.elems[1] = self.elems.pop()
    self.level = int(math.floor(math.log2(len(self.elems[1:])))) + 1
    self.percolate_down()
    return max_num

  def sort_heap(self):
    '''
    Sort the heap and print the sorted array
    '''
    if self.max_heap:
      sort_ar = [self.delete_max() for itr in range(len(self.elems[1:]))]
    else:
      sort_ar = [self.delete_min() for itr in range(len(self.elems[1:]))]
    self.elems = [0] + sort_ar
    self.level = int(math.floor(math.log2(len(self.elems[1:])))) + 1


def find_median(left_heap, right_heap, elem):
  '''
  '''
  left_heap.insert(elem)

  if left_heap.size - right_heap.size > 1:
    temp_elem =  left_heap.delete_max()
    right_heap.insert(temp_elem)

  if left_heap.size and right_heap.size:
    if left_heap.max_elem > right_heap.min_elem:
      left_elem = left_heap.delete_max()
      right_elem = right_heap.delete_min()
      left_heap.insert(right_elem)
      right_heap.insert(left_elem)

  # Find the median
  if left_heap.size > right_heap.size:
    median = round(float(left_heap.max_elem), 1)
  else:
    median = round((left_heap.max_elem + right_heap.min_elem) / 2, 1)

  return median


if __name__ == '__main__':
  n = int(input().strip())
  a = []
  a_i = 0
  for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

  # Create Heaps
  left_heap = Heap(max_heap=True)
  right_heap = Heap(max_heap=False)

  for elem in a:
    median = find_median(left_heap, right_heap, elem)
    print(median)
