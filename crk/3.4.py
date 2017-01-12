"""
__author__ = 'anyu'

In the classic problem of the Towers of Hanoi, you have 3 rods and N disks
of different sizes which can slide onto any tower. The puzzle starts with
disks sorted in ascending order of size from top to bottom (e.g., each disk sits
on top of an even larger one). You have the following constraints:

Only one disk can be moved at a time.
A disk is slid off the top of one rod onto the next rod.
A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first rod to the last using Stacks

ask again, are there any other requrirement? no? then recursion and implicit stack:)
stack explicitly is too hard and also the code will be cryptic

"""
def hanoi(n,src,med,des):
    if n ==1:
        print "move one disk from {} to {}".format(src,des)
    else:
        hanoi(n-1,src,des,med)
        print "move one disk from {} to {}".format(src,des)
        hanoi(n-1,med,src,des)

print hanoi(10, 'src', 'med', 'des')


def testhanoi():
    hanoi(1,'src','med','dst')

if __name__ == "__main__":
    testhanoi()
