#!/usr/bin/python  

def gensubstrings(s):
  for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
      yield s[i:j]

def substrings(s):
  return list(gensubstrings(s))

'''
Lists out the features for n.
Each feature is a string, indicating in binary a substring of the
binary representation of n. 'a' and 'z' indicate beginning and end
tokens.
A feature can appear more than once.
'''
def features(n):
  return substrings('a{0:b}z'.format(n))


class Vector:
  '''Make a vector by counting features.'''
  def __init__(self, feats):
    # The components maps features to a coefficient.
    self.components = {}
    for f in feats:
      self.components[f] = self.components.get(f, 0) + 1


def main():
  print substrings('football')
  

if __name__ == '__main__':
  main()
