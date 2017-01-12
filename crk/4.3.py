"""__author__ = 'anyu'

4.3 Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

One way to implement this is to use a simple root.insertNode(int v) method
This will indeed construct a tree with minimal height but it will not do so very efficiently.
Each insertion will require traversing the tree, giving a total cost of O(N log N) to the tree.

Alternatively, we can cut out the extra traversals by recursively using the createMinimalBST
method. This method is passed just a subsection of the array and returns the


Although this code does not seem especially complex, it can be very easy to make little off-by-one errors.
Besure to test these parts of the code very thoroughly  (But I DID NOT! ONE TIME FINISHED MASTERPIECE:) )

discuss that it automatically maintain a binary SEARCH tree here
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return "<" +str(self.left) + "<" +str(self.data) + ">" + str(self.right) + ">"



def creatbst(sortedarray):
    """
    O(n) running time?
    :param sortedarray:
    :return:
    """
    if len(sortedarray) == 0:
        return None
    elif len(sortedarray) == 1:
        return Node(sortedarray[0])
    else:
        mid = len(sortedarray)/2
        n = Node(sortedarray[mid])
        n.left=creatbst(sortedarray[:mid])
        n.right=creatbst(sortedarray[mid+1:])
        return n

intarray1=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515]
array = [1,2,3,4,5]
print creatbst(intarray1)
print creatbst(array)



class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

    def __str__(self):
        print(str(self.data))


    def insert(self,value):
        """
        insert a new value in to the current bst
        O(nlogn)
        :param value:
        :return:
        """
        if self.data == None:
            self.data = value
        elif self.data ==value:
            return False
        elif self.data> value:
            if self.left == None:
                self.left = Node(value)
                return True
            else:
                return self.left.insert(value)
        elif self.data <value:
            if self.right == None:
                self.right = Node(value)
                return True
            else:
                return self.right.insert(value)


