# Towers of Hanoi: In the classic problem of the  wers of Hanoi, you have 3 towers and N disks
# of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
#  of size from top to bottom (i.e., each disk sits on top of an even larger one).You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.

def hanoi(n, start="start", mid="mid", des="des"):
    if n ==1:
        print "move {} to {}".format(start, des)
        return
    else:
        hanoi(n-1, start, des, mid)
        print "move {} to {}".format(start, des)
        hanoi(n-1, mid, des, start)

hanoi(2)

def hanoiStack(n, start="start", mid="mid", des="des"):
