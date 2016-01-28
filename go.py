#!/usr/bin/python  

import math

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
If we can find a linear function of this vector that is always
positive, then that's the monovariant we are looking for.
'''
def diff(x):
  if x % 2 == 0:
    raise 'x must be an odd number'
  
  xprime = 3 * x + 1
  while xprime % 2 == 0:
    xprime /= 2

  # v and vprime are the feature vectors for x and -xprime
  v = Vector((b, 1) for b in features(x))
  vprime = Vector((b, -1) for b in features(xprime))

  answer = v + vprime
  if len(answer) == 0:
    raise Exception('diff(%d) has len zero' % x)
  return answer
  


'''
model is our model for the monovariant. The goal is that
model.dot(diff(x)) should always be positive.
example is diff(x) for some x.
This returns:
  (updated model, true) if it updates
  (same model, false) if it doesn't
I think this method is pretty close to the original perceptron method,
except it rounds up to the next integer for coefficients.
'''
def update(model, example):
  out = model.dot(example)
  if out > 0:
    return model, False

  # Add some of example to the model to make up for the shortfall
  shortfall = float(-out)
  norm = example.dot(example)
  if norm == 0:
    raise Exception('norm is 0 for a training example')
  needed = math.floor(shortfall / norm) + 1
  return (model + example.scale(needed), True)

'''
Returns the first n odd numbers, starting at 3.
'''
def odds(n):
  return range(3, 2 * n + 2, 2)
  
'''
Trains until they can all be classified positively.
'''
def train(samples):
  model = Vector()
  while True:
    updates = 0
    for sample in samples:
      model, updated = update(model, sample)
      if updated:
        updates += 1
    if updates == 0:
      break
    print 'learned from', updates, 'samples'
  return model

  
class Vector:
  '''
  For pairs, just treats each pair as a feature -> value entry.
  '''
  def __init__(self, pairs=()):
    # The components maps features to a coefficient.
    self.components = {}
    for f, v in pairs:
      new_value = self.components.get(f, 0) + v
      if new_value == 0:
        del self.components[f]
      else:
        self.components[f] = new_value

  def __add__(self, other):
    return Vector(self.components.items() + other.components.items())

  def scale(self, k):
    for key, val in self.components.items():
      self.components[key] = k * val

  def __len__(self):
    return len(self.components)
      
  def __sub__(self, other):
    return self + other.scale(-1)

  def __str__(self):
    def keyfn(item):
      key, count = item
      return (len(key), key)
    return '\n'.join(map(str, sorted(
      self.components.items(),
      key=keyfn)))

  def dot(self, other):
    answer = 0
    for f, v in self.components.items():
      answer += v * other.components.get(f, 0)
    return answer


def main():
  n = 100
  odd_numbers = odds(n)
  vectors = [diff(x) for x in odd_numbers]
  m = train(vectors)
  print m
  

if __name__ == '__main__':
  main()
