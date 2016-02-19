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
"""
def hanoi(n,src,med,destination):
    """
    n disks on A, move them to C
    using recursion,using stack implicitly
    """
    if n == 1:
        print "mov {} from {} to {}".format(n, src, destination)
        return
    else:
        hanoi(n-1,src,destination,med)
        print "mov {} from {} to {}".format(n, src, destination)
        hanoi(n-1,med,src,destination)
    return

"""
stack explicitly is too hard and also the code will be cryptic
void hanoi(int n, char src, char bri, char dst){
    stack<op> st;
    op tmp;
    st.push(op(1, n, src, bri, dst));
    while(!st.empty()){
        tmp = st.top();
        st.pop();
        if(tmp.begin != tmp.end){
            st.push(op(tmp.begin, tmp.end-1, tmp.bri, tmp.src, tmp.dst));
            st.push(op(tmp.end, tmp.end, tmp.src, tmp.bri, tmp.dst));
            st.push(op(tmp.begin, tmp.end-1, tmp.src, tmp.dst, tmp.bri));
        }
        else{
            cout<<"Move disk "<<tmp.begin<<" from "<<tmp.src<<" to "<<tmp.dst<<endl;
        }

    }
}
"""



def testhanoi():
    hanoi(1,'src','med','dst')

if __name__ == "__main__":
    testhanoi()