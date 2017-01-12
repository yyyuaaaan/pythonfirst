"""

__author__ = 'anyu'

Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start a new
stack when the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several stacks,
and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack (that is, pop() should return the same values as it would if there were just a single stack).

followup
Implement a function popAt(int index) which performs a pop operation on a speci c sub-stack.

You could make an argument that, rather than "rolling over,"
we should be OK with some stacks not being at full capacity.
There's no "right answer" here; you should discuss this
trade-off with your interviewer.


This problem is not conceptually that tough,
but it requires a lot of code to implement it fully.
Your interviewer would not ask you to implement the entire code.

A good strategy on problems like this is to separate code into other methods,
like a lefts h if t method that pop At can call.This will make your code cleaner
and give you the opportunity to lay down the skeleton of the code before
dealing with some of the details.
"""

# below is too complex!!! implement a single normal stack class first,which take a array parameter,
# then let Set_Of_Stacks inherited this Stack class, do it like 3.2, much easier


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

class SetsofStack(object):
    '''
    conposition over inheritance
    use hash() of item to decide which substack to use, automatic loadbalance

    '''
    def __init__(self, sizeofonestack=20, nofstacks=3):
        self.nofsets=3
        self.stacks=[]
        for i in range(nofstacks):
            self.stacks.append(Stack(sizeofonestack))

    def push(self,data):
        indexofstack=hash(data)
        if self.stacks[indexofstack].full():
            print("stack full")
        else:
            self.stacks[indexofstack].push(data)

    def pop(self, i):
        if self.stacks[i].empty():
            print("stack empty")
        else:
            return self.stacks[i].pop()

class SetsofStack(object):
    def __init__(self,nofstacks=3,sizeofonestack=10):

        self.stacks=[]
        for i in range(nofstacks):
            self.stacks.append(Stack(sizeofonestack))
        self.setspointer=-1
        self.size = nofstacks * sizeofonestack

    def empty(self):
        return self.setspointer== -1
    def full(self):
        return self.setspointer==self.size-1

    def push(self,data):
        if self.full():
            return
        else:
            indexofstack=self.sp/self.stacks[0].size
            self.stacks[indexofstack].push(data)
            self.sp +=1
            return

    def pop(self):
        if self.empty():
            return
        else:
            indexofstack=self.sp/self.stacks[0].size
            item = self.stacks[indexofstack].pop()
            self.sp -=1
            return item

