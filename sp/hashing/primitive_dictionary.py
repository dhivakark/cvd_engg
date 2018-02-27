class dictionary:
  def __init__(self, size = 20):
    self.size = size
    self.hash_table = [('', '') for i in range(size)]

  def __hash_function(self , key, trail_no):
    hash_value = (sum([ord(character) for character in key]) + trail_no) %\
                  self.size
    return hash_value

  def insert(self, (key, value)):
    for trail_no in range(self.size):
      hash_value = self.__hash_function(key, trail_no)
      if self.hash_table[hash_value][0] == '':
        self.hash_table[hash_value] = (key, value)
        break
      elif self.hash_table[hash_value][0] == ('Deleted'):
        self.hash_table[hash_value] = (key, value)
        break
      elif self.hash_table[hash_value][0] == key:
        self.hash_table[hash_value] = (key, value)
    return

  def delete(self, key):
    '''
    '''
    for trail_no in range(self.size):
      hash_value = self.__hash_function(key, trail_no)
      if self.hash_table[hash_value][0] == key:
        self.hash_table[hash_value] = (('Deleted'), '')
        return
    else:
      print('key :{} not found, hence cannot be deleted'.format(key))

  def search(self, key):
    '''
    '''
    for trail_no in range(self.size):
      hash_value = self.__hash_function(key, trail_no)
      if self.hash_table[hash_value][0] == key:
        return self.hash_table[hash_value][1]
    else:
      print('key :{} not found, hence cannot be deleted'.format(key))

def main():
  '''
  '''
  dictnry = dictionary(20)
  dictnry.insert(('rat', 20))
  dictnry.insert(('cat', 50))
  print(dictnry.search('rat'))
  dictnry.delete('rat')
  dictnry.search('rat')


if __name__ == '__main__':
    main()


