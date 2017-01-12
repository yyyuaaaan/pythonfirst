"""

__author__ = 'anyu'

3.1 Describe how you could use a single array to implement three stacks.
可以以数组的头和尾作为栈底分别维护两个栈，然后第三个栈以数组中间位置作为栈底，
左右交替入栈，当有栈顶碰撞时作为溢出处理。可能比较非主流的想法。。但实现麻烦, flexible in size!!!
Alternatively, we can be flexible in our space allocation,
but this significantly increases the complexity of the problem
 Fixed Division
int stackSize = 100;

hash the item and devide by 3, remainder decide which stack to put in


"""
class Stack(list):
    def __init__(self, size=10):
        self.size=size
        self.stack=[]

    def empty(self):
        return self.stack.__len__()==0
    def full(self):
        return self.size==self.stack.__len__()

    def push(self,data):
        if self.full():
            print("stack full")
        else:
            self.stack.append(data)
    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            data = self.stack.pop()
            return data

class ArrayForThreeStacks(object):
    """
    # wrong, -1 is actually empty
    """
    def __init__(self,sizeofarray=120,nofstacks=3):
        self.array=[None]*sizeofarray
        self.nofstacks=nofstacks
        self.indexofstacks=[]
        for i in range(self.nofstacks):
            self.indexofstacks.append(0)

    def empty(self,stacknumber): #0 1 2
        return self.indexofstacks[stacknumber]==0

    def full(self,stacknumber):
        return self.indexofstacks[stacknumber] == len(self.array)/self.nofstacks

    def push(self,stacknumber,data):
        if self.full(stacknumber):
            print("stack full")
            return
        else:
            sizeofonestack = len(self.array)/self.nofstacks
            self.array[stacknumber*sizeofonestack + self.indexofstacks[stacknumber]] = data
            self.indexofstacks[stacknumber]+=1
            return

    def pop(self,stacknumber):
        if self.empty(stacknumber):
            print("stack empty")
            return
        else:
            sizeofonestack = len(self.array)/self.nofstacks

            i = sizeofonestack*stacknumber + self.indexofstacks[stacknumber]
            self.indexofstacks[stacknumber] -=1

            return self.array[i]
