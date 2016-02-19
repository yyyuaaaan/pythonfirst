"""

__author__ = 'anyu'

How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element? Push,
pop and min should all operate in O(1) time.


solution 1: priority queue, no, push is ok, when we pop, looking for the next min will take more than O(1)
solution 2 change stack item to (iter,min) tuper, costly
solution 3. Use an additional python list to keep track of mins (Save space)

"""


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

class Stackmin(object):
    """
    more concise, only need to change the pop push, and add a trivial getmin
    do not forget goddam self!
    """
    def __init__(self, size):
        self.size=size
        self.sp=-1
        self.stack=[None]*size
        self.minlist=[None]*size

    def empty(self):
        return self.sp==-1
    def full(self):
        return self.sp==self.size-1
    def push(self,data):
        if self.full():
            print("stack full")
        else:
            if not self.minlist:
                if data>=self.minlist[self.sp]:
                    self.minlist[self.sp+1]=self.minlist[self.sp]
                else:
                    self.minlist[self.sp+1]=data
            self.sp+=1
            self.stack[self.sp] = data
    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            data = self.stack[self.sp]
            self.sp-=1
            return data

    def min(self):
        if not self.empty():
            return self.minlist[self.sp]