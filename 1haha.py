"""
不要在iterate list 的时候改变它的值，会出错，要clone这个list再做操作。
	for e1 in L1[:]:         #在iterate的时候，拷贝一下list

class BinaryTreeNode: # this will not work,python do not suppurt pointer, and recursion

    def __init__(self,value=0):
        self.value = value
        self.left = BinaryTreeNode()
        self.right = BinaryTreeNode()

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

"""__author__ = 'anyu'
hard

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

        m = re.match(r'^[\s]*([0-9]*\.?[0-9]*)([Ee][+-]?[0-9]+)?[\s]*$', s)
class Solution {
public:
    bool isNumber(const char *s) {
        enum InputType {INVALID, SPACE, SIGN, DIGIT, DOT, EXPONENT};
        int transitionTable[][SPACEEND] =
        { /* 0   1   2   3   4   5  */
             0,  1,  2,  3,  4,  0, // 0: INVALID
             0,  1,  2,  3,  4,  0, // 1: SPACE
             0,  0,  0,  3,  4,  0, // 2: SIGN
             0,  6,  0,  3,  7,  5, // 3: DIGIT
             0,  0,  0,  7,  0,  0, // 4: DOT
             0,  0,  2,  8,  0,  0, // 5: EXPONENT
             0,  6,  0,  0,  0,  0, // 6: END WITH SPACE
             0,  6,  0,  7,  0,  5, // 7: DOT AND DIGIT
             0,  6,  0,  8,  0,  0, // 8: END WITH SPACE OR DIGIT
        };

        InputType last = INVALID;
        while (*s != '\0')
        {
            InputType state = INVALID;
            if (*s == ' ')
                state = SPACE;
            else if (isdigit(*s))
                state = DIGIT;
            else if (*s == '+' || *s == '-')
                state = SIGN;
            else if (*s == 'e')
                state = EXPONENT;
            else if (*s == '.')
                state = DOT;
            last = (InputType) transitionTable[last][state];
            if (last == INVALID) return false;
            s++;
        }
        bool validFinal[] = {0, 0, 0, 1, 0, 0, 1, 1, 1};
        return validFinal[last];
    }
};
'"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        d =['0','1','2','3','4','5','6','7','8','9']
        t=s.strip()
        if " " in t:
            return False
        if t.find(".") is not -1:
            i = t.find(".")
            if t[0] is '.' or t[len(t)-1] is '.': return False
            if t[i+1:].find(".") is not -1: return False
            if t[i-1] not in d or t[i+1] not in d: return False
        if t.find('e') is not -1:
            j = t.find('d')
            if '.' in t[j-1:]: return False
        return True

"""
Divide two integers
Divide two integers without using multiplication, division and mod operator.

        // special case when denominator == INT_MIN
zero devision
negative

simplify be integer devision

recursion div(a -b,b)+1

"""
"""
Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Use a stack to keep track of the positions of non-matching '('s. Also need to keep track of the position of the last ')'.
find the first "(" left paren first
"""

"""
3Sum
我喜欢暴力破解，itertools.combinations(S,3) O(n3),
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
For example, given array S = [-1,0,1,2,-1,-4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def threeSumClosest(array, target):
    array.sort()
    size = len(array)
    if size<3: return
    result = [1 << 33, -1, -1, -1]  # a large number
    for first in range(size - 2):
        left = first + 1
        right = size - 1
        while left < right:
            curr = array[first] + array[left] + array[right]
            distance = abs(curr - target)
            if distance < result[0]:
                result = [distance, array[first], array[left], array[right]]
            if curr < target:
                left += 1
            else:
                right -= 1
    if distance is 0: return result[1:]
    else:
        print "no such combination"
        return



"""
Word Ladder, bfs, edit distance
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""
def ladderLength(start, end, words):
        words.append(start)
        words.append(end)
        n = len(start)
        d = {}

        for w in words:
            d[w] = 0;
        d[start] = 1;

        q = collections.deque()
        q.append(start)

        while q:
            s = q.popleft()
            chars = list(s)
            for i in range(n):
                head = ''.join(chars[0:i])
                tail = ''.join(chars[i + 1:n])

                for j in range(ord('a'), ord('z')):
                     t = head + chr(j) + tail
                     if t in d and d[t] == 0:  # no visted, d[x] ==0  is not visited
                        d[t] = d[s] + 1
                        q.append(t)
                        if t == end: return d[t]
        return 0


"""__author__ = 'anyu'
 A message containing letters from A-Z is being encoded to numbers using the following mapping:
 'A' -> 1
 'B' -> 2
 ...
 'Z' -> 26
 Given an encoded message containing digits, determine the total number of ways to decode it.
 For example,
 Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 The number of ways decoding "12" is 2.

 Solution: dp. Note that '0' must be decoded in together with the number in front of it.
 """
def num_decodings(s):
    if not s or s[0] is "0":
        return 0
    n = len(s)
    dp = [None]*n+1
    dp[0]=1
    for i in range(1,n+1):
        if s[i-1] <'0' or s[i-1]>'9': return 0
        if s[i-1] is not '0': dp[i] = dp[i-1]
        if i>1 and (s[i-2] is '1' or (s[i-2] is '2' and s[i-1]<='6')):
            dp[i]+= dp[i-2]
        if dp[i] is 0: return 0

    return  dp[n]

"""
# There are N children standing in a line. Each child is assigned a rating
# value.

# You are giving candies to these children subjected to the following
# requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
"""
def candy(ratings):
    ratings.sort()
    total = 0
    currR, currC = ratings[0], 1
    for r in ratings:
        if r > currR:
            currR = r
            currC += 1
        total += currC
    return total

ratings = [2, 3, 4, 4, 1, 1, 1]
print candy(ratings)

"""
Pascal's Triangle II
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
滚动数组实现。注意Line11，要从后往前加，否则会产生冗余计算。

"""

"""
 Sort a linked list in O(nlogn) time using constant space complexity.

 Solution: merge sort.

class Solution {
public:
    ListNode *sortList(ListNode *head) {
        return sortLinkedList(head, getLength(head));
    }

    ListNode* sortLinkedList(ListNode *&head, int N) {
        if (N == 0) return NULL;
        if (N == 1) {
            ListNode* cur = head;
            head = head->next;
            cur->next = NULL;
            return cur;
        }
        int half = N / 2;
        ListNode* head1 = sortLinkedList(head, half);
        ListNode* head2 = sortLinkedList(head, N - half);
        return mergeList(head1, head2);
    }

    ListNode* mergeList(ListNode *head1, ListNode*head2) {
        ListNode dummy(0); dummy.next = NULL;
        ListNode *cur = &dummy;
        while (head1 && head2)
        {
            ListNode **min = head1->val < head2->val ? &head1 : &head2;
            cur->next = *min;
            cur = cur->next;
            *min = (*min)->next;
        }
        if (!head1) cur->next = head2;
        if (!head2) cur->next = head1;
        return dummy.next;
    }

    int getLength(ListNode *head) {
        int length = 0;
        while (head) {
            length++;
            head = head->next;
        }
        return length;
    }
};
"""
def pow(x,n):
    if n ==0:
        return 1
    elif n%2==1:
        return x*(pow(x,(n-1)/2))**2
    else:
        return pow(x,n/2)**2

def EleminateDuplicate(data): #shuzu eliminate dups
    if not data
        return data

    lastNonduplicate = 0
    while i in range(1, len(data)) :
        if data[i] != data[lastNonduplicate]
            lastNonduplicate += 1
            data[lastNonduplicate] = data[i]
        i += 1

    return data, lastNonduplicate

def twosum(data, sum):
    """
    sorted array
    """
    if not data:
        return None
    else:
        res=[]
        front=0
        end=len(data)-1

        while front <= end:
            if data[front] +[end]==sum:
                res.append((data[front],data[end]))
            elif data[front] +[end]<sum:
                front+=1
            else:
                end-=1

        return res

