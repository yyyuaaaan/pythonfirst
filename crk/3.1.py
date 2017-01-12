"""

__author__ = 'anyu'

3.1 Describe how you could use a single array to implement three stacks.
可以以数组的头和尾作为栈底分别维护两个栈，然后第三个栈以数组中间位置作为栈底，
左右交替入栈，当有栈顶碰撞时作为溢出处理。可能比较非主流的想法。。但实现麻烦, flexible in size!!!
Alternatively, we can be flexible in our space allocation,
but this significantly increases the complexity of the problem
 Fixed Division
int stackSize = 100;


"""
class ArrayForThreeStacks(object):
    """
    # wrong, -1 is actually empty
    """
    def __init__(self,llist):
        self.array=[None]*100
        self.number=0 # front, middle, end stack correspont 0, 1, 2
        self.frontstack=self.array[0]
        self.frontstacksize=30
        self.frontstackpointer=0

        self.endstack=self.array[99]
        self.endstacksize=30
        self.endstackpointer=30 # array[30]-[69]

        self.middlestack=self.array[30]
        self.middlestacksize=40
        self.middlestackpointer=70

    def empty(self,stacknumber):
        if stacknumber ==0:
            return self.frontstackpointer==0
        elif stacknumber ==1:
            return self.endstackpointer == 30
        elif stacknumber ==2:
            return self.middlestackpointer==70
        else:
            print("wrong parameter")
            return

    def full(self,stacknumber):
        if stacknumber ==0:
            return self.frontstackpointer==29
        elif stacknumber ==1:
            return self.endstackpointer == 69
        elif stacknumber ==2:
            return self.middlestackpointer==99
        else:
            print("wrong parameter")
            return

    def push(self,stacknumber,data):
        if self.full(stacknumber):
            print("stack full")
            return
        else:
            if stacknumber ==0:
                self.array[self.frontstackpointer]=data
                self.frontstackpointer+=1
            elif stacknumber ==1:
                self.array[self.middlestackpointer]=data
                self.frontstackpointer+=1
            elif stacknumber ==2:
                self.array[self.endstackpointer]=data
                self.frontstackpointer+=1
            return

    def pop(self,stacknumber):
        if self.empty(stacknumber):
            print("stack empty")
            return
        else:
            if stacknumber ==0:
                data= self.array[self.frontstackpointer]
                self.frontstackpointer-=1
            elif stacknumber ==1:
                data=self.array[self.middlestackpointer]
                self.frontstackpointer-=1
            elif stacknumber ==2:
                data=self.array[self.endstackpointer]
                self.frontstackpointer-=1
            return data




