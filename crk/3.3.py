"""

__author__ = 'anyu'

h.......
Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start a new
stack when the previous stack exceeds some threshold. Implement a data structure
SetOfStacks that mimics this. SetOfStacks should be composed of several stacks,
and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack (that is, pop() should return the same values as it would if there were just a single stack).

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
class Set_Of_Stacks(object):
    def __init__(self,stacksize=100,stackthreshold=80):
        self.stackbottom = [None]*1000
        self.stacksize=stacksize
        self.stackthreshold= stackthreshold
        self.sp=0
        self.numofset=1

    def isempty(self,sp):
        return sp%100==0

    def isfull(self,sp):
        return sp%80==0

    def push(self,value):
        if self.isfull(self.sp)== True:
            self.sp += 20
            self.stackbottom[self.sp]=value
            self.numofset += 1
        else:
            self.sp+=1
            self.stackbottom[self.sp]=value
            self.numofset+=1

    def pop(self):
        if self.isempty:
            if self.sp==0:
                print "stack void"
                return
            else:
                 v = self.stackbottom[self.sp-20]
                 self.sp -= 20
                 self.numofset -= 1
                 return v
        else:
            v=self.stackbottom[self.sp]
            self.sp -= 1
            return v

    def popat(self,index): # assume stack index starts from 1 to 2,3...
        """
        do not consider space redundency and waste,
        push is the same
        pop need to change. by check if None

        """
        if index<1 or index > self.numofset:
            print "index out of bounds"
            return
        if self.sp//100 == 0:
            return self.pop()
        else:
            v = self.stackbottom[80+100*(index-1)]
            self.stackbottom[80+100*(index-1)] = None
            return v


#---------- test
def test_set_of_stack():
    setsofstack = Set_Of_Stacks()
    for i in range(50):
        setsofstack.push(i)

    for i in range(5):
        print "Poped", setsofstack.pop()
    return

if __name__ == "__main__":
    test_set_of_stack()




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

class SetsofStack(Stack):
    def __init__(self,size=100,capacity=50, nofsets=0):
        self.size=size
        self.capacity=50
        self.nofsets=0
        self.stack=[None]*self.capacity
        self.stack2=[None]*self.capacity

    def push(self,data):
        if self.full():
            print("stack full")
        else:
            self.sp+=1
            if self.sp/50==0:
                self.stack[self.sp] = data
            else:
                self.nofsets=self.sp/50
                self.stack2[(self.sp)/self.capacity] = data

    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            if self.sp<self.capacity:
                data = self.stack[self.sp]
                self.sp-=1
            else:
                data = self.stack2[self.sp/self.capacity]
                self.sp -=1
            return data
