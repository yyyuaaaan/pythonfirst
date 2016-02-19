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


class myqueueforfun(object):
    def __init__(self):
        self.stk1=[]
        self.stk2=[]
        self.qfrond=0
        self.qend=0
        self.size = 10

    def enqueue(self,value):
        if self.isfull():
            print "queue full"
        elif self.stk1 == [] and self.stk2 !=[] :
            while self.stk2 != []:
                self.stk1.append(self.stk2.pop())
            self.stk1.append(value)
            self.qfrond += 1
        else:
            self.stk1.append(value)
            self.qfrond += 1
        return

    def dequeue(self):
        if self.isempty():
            print "queue empty!"
            return
        else:
            if len(self.stk2)>len(self.stk1):
                v = self.stk2.pop()
            else:
                v = self.stk1.pop()
            self.qfrond -= 1
            return v


    def isempty(self):
        return self.stk1==[] and self.stk2 == []

    def isfull(self):
        return self.qfrond == 10



q1 = myqueueforfun()

q2 = myqueueforfun()

#testing
from random import randrange
for step in xrange(20):
	operation = randrange(10)
	if operation < 7:
		q1.enqueue(operation)
		q2.enqueue(operation)
		print "push", operation
	elif not q2.isempty():
		print "pop", q1.dequeue(), q2.enqueue(operation)



class Stack(object):
    def __init__(self, size):
        self.size=size
        self.sp = -1
        self.stack=[None]*size

    def empty(self):
        return self.sp==-1
    def full(self):
        return self.sp==self.size-1
    def push(self,data):
        if self.full():
            print("stack full")
        else:
            self.sp+=1
            self.stack[self.sp] = data
    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            data = self.stack[self.sp]
            self.sp-=1
            return data

class MyQueue(Stack):
    """
    class stack has sp, full, empty, push, pop method
    size = 50
    naive method
    """
    def __init__(self,size):
        self.size = size
        self.s1=Stack(size) # stack use only for reverse order and pop
        self.s2=Stack(size) #main queque for storage
        self.qpointer=-1

    def empty(self):
        return self.qpointer== -1

    def full(self):
        return self.qpointer == self.size - 1

    def enqueue(self,data):
        if self.full():
            print("full")
            return
        if not self.full():
            self.s2.push(data)
            self.qpointer+= 1
            return
    def deque(self):
        """
        every time do pop, reverse order with s1,
        and after one pop, put all data in s2 again
        not efficient, when do pop continuously, but clear
        :return:
        """
        if self.empty():
            print("empty")
            return
        if not self.empty():
            while self.s2.sp != -1:
                data = self.s2.pop()
                self.s1.push(data)
            resdata = self.s1.pop()

            while self.s1.sp != -1:
                temp = self.s1.pop()
                self.s2.push(temp)
            return resdata