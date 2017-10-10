import sys


def find_total_inversion(A):
  if len(A)== 1:
    return 0
  sorted_array, inv_count = count_inversion(A)
  return inv_count
  
def count_inversion(A):
  if len(A) <= 1:
    return A, 0
  left = []
  right = []
  left = A[:len(A) // 2]
  right = A[len(A) // 2: ]
  left, count_inv_left = count_inversion(left)
  right, count_inv_right = count_inversion(right)
  merge_array, inv_count = merge(left, right)
  inv_count += count_inv_left + count_inv_right
  return merge_array, inv_count

def merge(left, right):
    result = []
    inv_count = 0
    while left and right:
      if left[0] <= right[0]:
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]
        inv_count += len(left)
    if left:
      result += left
    if right:
      result += right
    return result, inv_count
  
  

def countInversions(arr):
    return find_total_inversion(arr)
    

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    countInversions(arr)
    #t = int(raw_input().strip())
    #for a0 in xrange(t):
    #    n = int(raw_input().strip())
    #    arr = map(int, raw_input().strip().split(' '))
    #    result = countInversions(arr)
    #    print result
