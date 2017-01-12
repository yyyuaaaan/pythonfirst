"""
__author__ = 'anyu'

3.5 Implement a MyQueue class which implements a queue using two stacks.
We can use our second stack to reverse the order of the elements (by popping s i

We can implement a “lazy” approach where we let the elements sit in s2
s1 will thus be ordered with the newest elements on the top, while s2 will have the oldest
elements on the top. We push the new elements onto s1, and peek and pop from s2.
When s2 is empty, we’ll transfer all the elements from s1 onto s2, in reverse order.
size undetermined from size of 1 stack to 2 stack
full= only need s1 is full
empyt need s1 and s2 to be empty

During your actual interview, you may find that you forget the exact API calls.
Don't stress too much if that happens to you. Most interviewers are okay with
your asking for them to refresh your memory on little details.
They're much more concerned with your big picture understanding.

"""

class MyQueue(object):
    """
    my design is enque friendly, if do the complex design, both enque and deque takes O(n) and more complex
    """
    def __init__(self, size=20):
        """
        one stack push, another stack pop
        :param size:
        """
        self.stack1=[]
        self.stack2=[] # temp to pop
        self.queuesize=size/2
        self.queueindex=0

    def empty(self):
        return self.queueindex==0

    def full(self):
        return self.queueindex== self.queuesize

    def push(self,data):
        if  self.full():
            return
        else:
            self.stack1.append(data)

    def pop(self):
        if self.empty():
            return
        else:
            while self.stack1:
                self.stack2.append(self.stack1)
            item = self.stack2.pop()

            while self.stack2:
                self.stack1.append(self.stack1)
