class BST(object):
  def __init__(self, k ):
    self.root = None
    self.interval = k

  def insert(self, element ):
    new = BSTnode(element)
    if self.root == None:
      self.root = new
    else:
      node = self.root
      while True:
        if( abs(node.element - element) <= self.interval):
          print 'Ignoring element %d due to clash'%(element)
          break
        if element <  node.element:
          if node.left == None:
            new.parent = node
            node.left = new
            print 'Inserted element %d'%(element)
            break
          node = node.left

        else:
          if node.right == None:
            new.parent = node
            node.right = new
            print 'Inserted element %d'%(element)
            break
          node = node.right

  def find_min(self):
    node = self.root
    if node == None:
      return None
    else:
      while node.left != None:
          node = node.left
      return node

  def delete( self, time):
    min_node = self.find_min()
    if min_node:
      if min_node.element == time:
        print("deleting element", min_node.element)
        if min_node.parent == None:
          self.root = min_node.right
        else:
          min_node.parent.left = min_node.right
          if min_node.right != None:
            min_node.right.parent = min_node.parent
          min_node.disconnect()

class BSTnode(object):
    def __init__(self, t):
        self.element = t
        self.left = None
        self.right = None
        self.parent = None

    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None
        self.element = None

def build_BST(landings):
    bst = BST(4)
    time = -1
    for landing in landings:
        time += 1
        print("time:",time)
        for ins_time in landing:
          bst.insert(ins_time)
        bst.delete(time)

if __name__ == '__main__':
    landings = [[2],
                [11, 13, 15, 17],
                [3,5,7,8],
                [10, 12, 20, 30],
                [23, 25, 5, 1]]
    build_BST(landings)

