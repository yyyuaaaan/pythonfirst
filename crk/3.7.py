"""
__author__ = 'anyu'

An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain
this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the builtin LinkedList data structure.

single linkedlist, dequeue complex
two linkedlist, have to maintain a timestamp

"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextnode = None

# linkedlist node is type Node as defined

class FunnyQueue(Node):
    def __init__(self):
        self.quequefront = Node(None) # first dummy node None
        self.quequeend = self.quequefront

    def empty(self):
        return self.quequefront == self.quequeend

    def enque(self,data):
        if data == "cat":
            tempnode = Node("cat")
            self.quequeend.nextnode = tempnode
            self.quequeend = self.quequeend.nextnode
        elif data == "dog":
            tempnode = Node("dog")
            self.quequeend.nextnode = tempnode
            self.quequeend = self.quequeend.nextnode
        else:
            print("wrong input")
        return

    def dequeany(self):
        if self.quequefront.nextnode is not None:
            temp = self.quequefront.nextnode.data
            self.quequefront ==self.quequefront.nextnode
            self.quequefront.data == None # front become dummy node again
            return temp
        else:
            print "queque empty"
            return

    def dequecat(self):
        """
        dequedog same, dont repeat
        :return:
        """
        if self.quequefront.nextnode is  None:
            print("queque empty")
            return
        else:
            p1 = self.quequefront
            p2 = self.quequefront.nextnode
            while p2:
                if p2.data == "cat":
                    p1.nextnode = p2.nextnode
                    p2.nextnode=None
                    break
                else:
                    p2 = p2.nextnode
                    p1= p1.nextnode

            if p2.data =="cat":
                return p2
            else:
                print("no cat node")
                return


