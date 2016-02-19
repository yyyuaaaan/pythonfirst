"""__author__ = 'anyu'
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
def powerset(myset):
    """
    as about non-descending order, sort() each element in subset
    """
    result = [[]]
    for element in myset:
        result += [subset + [element] for subset in result] # result.extend() also ok
    return result

def subsets(data):
    def _subsets(step):
        results.append(list(path))
        for i in range(step, len(data)):
            if i != step and data[i] == data[i - 1]:
                continue
            path.append(data[i])
            _subsets(i + 1)
            path.pop()
    data.sort()
    results = []
    path = []
    _subsets(0)
    for i in results:
        print(i)