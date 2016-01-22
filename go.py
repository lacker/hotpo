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


'''
x should be an odd number.

Makes a vector for x-features minus (xprime)-features,
where xprime has had one step of HOTPO applied.
If we can find a +/- symmetric function of this vector that is always
positive, then that's the monovariant we are looking for.
'''
def diff(x):
  xprime = 3 * x + 1
  while xprime % 2 == 0:
    xprime /= 2

  # v and vprime are the feature vectors for x and -xprime
  v = Vector((b, 1) for b in features(x))
  vprime = Vector((b, -1) for b in features(xprime))

  return v + vprime
  
  
class Vector:
  '''
  For pairs, just treats each pair as a feature -> value entry.
  '''
  def __init__(self, pairs):
    # The components maps features to a coefficient.
    self.components = {}
    for f, v in pairs
      self.components[f] = self.components.get(f, 0) + v

  def __add__(self, other):
    return Vector(self.components.items() + other.components.items())

  def scale(self, k):
    for key, val in self.components.items():
      self.components[key] = k * val

  def __sub__(self, other):
    return self + other.scale(-1)
    

def main():
  print substrings('football')
  

if __name__ == '__main__':
  main()
