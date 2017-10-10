import re
import numpy as np

def read_document(path):
  with open(path, 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
  return data.lower()

def remove_spcl_char(string):
  #result = re.sub('[^0-9]','', a)
  result = re.sub('[^0-9^a-z^A-Z ]','', string)
  result = result.split(' ')
  result = list(filter(lambda x: x!= '', result))
  return result

def compute_word_list(word_list1, word_list2):
  ttl_words = []
  ttl_words += list(set(word_list1).union(word_list2))
  word_idx = dict(zip(ttl_words,[i for i in range(len(ttl_words))])) 
  return word_idx

def calculate_word_vector(word_dict, doc_words):
  word_vector = np.zeros(len(word_dict))
  for word in word_dict:
    idx = word_dict[word]
    word_vector[idx] += 1
  return word_vector



def compute_doc_dst(vector1, vector2):
  similarity = np.dot( vector1, vector2)
  print similarity
  print np.linalg.norm(vector1)
  print np.linalg.norm(vector2)
  similarity = float(similarity) / np.linalg.norm(vector1) / np.linalg.norm(vector2)
  return similarity

def main(path1, path2):
  print path1
  print path2
  doc1 = remove_spcl_char(read_document(path1))
  doc2 = remove_spcl_char(read_document(path2))
  word_dict = compute_word_list(doc1, doc2)
  print word_dict
  word_vector1 = calculate_word_vector(word_dict, doc1)
  word_vector2 = calculate_word_vector(word_dict, doc2)
  print np.array_equal( word_vector1, word_vector2)
  similarity = compute_doc_dst( word_vector1, word_vector2)
 # print similarity
 


  

if __name__ == '__main__':
  path1 = '/Users/haemanth/work/eng_lunch/datasets/t3.lewis.txt'
  path2 = '/Users/haemanth/work/eng_lunch/datasets/t2.bobsey.txt' 
  main(path1, path2)
