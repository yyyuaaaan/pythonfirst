"""
不要在iterate list 的时候改变它的值，会出错，要clone这个list再做操作。
	for e1 in L1[:]:         #在iterate的时候，拷贝一下list

L1=[1, 2, 3, 4]
L2=[1,2,5,6]

class BinaryTreeNode: # this will not work,python do not suppurt pointer, and recursion

    def __init__(self,value=0):
        self.value = value
        self.left = BinaryTreeNode()
        self.right = BinaryTreeNode()

stable sorting is good, donot exchange equal keys,

Sorting by insertion
Sorting by selection
Sorting by exchange


Unit test：会用stubs, 当软件还不存在，simulate来测试
L.sort 改变了list， sorted不改变list，return一个新的list
如果对dict 做sorted返回一个keys的list，如果用dict.sort,会出exception，因为dict没有sort

Some general rules of testing:
A testing unit should focus on one tiny bit of functionality and prove it correct.
Each test unit must be fully independent. Each of them must be able to run alone, and also within the test
suite, regardless of the order they are called. The implication of this rule is that each test must be loaded
with a fresh dataset and may have to do some cleanup afterwards. This is usually handled by setUp() and
tearDown() methods.
Try hard to make tests that run fast. If one single test needs more than a few millisecond to run, development
 will be slowed down or the tests will not be run as often as desirable. In some cases, tests can’t be fast
 because they need a complex data structure to work on, and this data structure must be loaded every time
  the test runs. Keep these heavier tests in a separate test suite that is run by some scheduled task, and
  run all other tests as often as needed.
Learn your tools and learn how to run a single test or a test case. Then, when developing a function inside
a module, run this function’s tests very often, ideally automatically when you save the code.
Always run the full test suite before a coding session, and run it again after. This will give you more
confidence that you did not break anything in the rest of the code.
It is a good idea to implement a hook that runs all tests before pushing code to a shared repository.
The first step when you are debugging your code is to write a new test pinpointing the bug. While it is not
 always possible to do, those bug catching test are among the most valuable pieces of code in your project.
Use long and descriptive names for testing functions.
Regression testing
The intent of regression testing is to ensure that a change such as those mentioned above has not introduced
new faults.[1] One of the main reasons for regression testing is to determine whether a change in one part
 of the software affects other parts of the software.[2]

Unit Test Libraries
The reasons why I choose and continue to use py.test are the simple test collection, the lack of boilerplate
 and the ability to define set up and tear down functions at test, class or module level. For example for this
  function:
	def parse_connection(connection_string):
	    pass

Whilst the same test in py.test is more simple:
	from parse_conn import parse_connection
	import py.test

	def test_not_at():
    	py.test.raises(ValueError, parse_connection, 'invalid uri')
"""


import py.test
#One more feature of py.test that is really useful is the ability to run all the tests in a subdirectory.

def test_div_zero():
    py.test.raises(ZeroDivisionError, "1/0")


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_simple():
    assert "42 is the answer" == str(42) + " " + "is the answer"


def test_multiply():
    assert 42 == 6 * 7


def test_ord():
    assert ord('a') + 1 == ord('b')



if __name__ == '__main__':
    pytest.main()



def bsearch(l, value):
    """
    shoude have left right index, and have a different solution see9.3
    :param l:
    :param value:
    :return:
    """
    lo, hi = 0, len(l)-1
    while lo <= hi:
        mid = (lo + hi) / 2
        if l[mid] < value:
            lo = mid + 1
        elif value < l[mid]:
            hi = mid - 1
        else:
            return mid
    return -1
a = [1, 2, 3, 5, 9, 11, 15, 66]
print bsearch(a,7)




def merge_sort(A):
    """
    Sort list A into order, and return result.
    wrong
    """
    n = len(A)
    if n==1:
        return A
    mid = n//2     # floor division
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

