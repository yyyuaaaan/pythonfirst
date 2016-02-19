"""__author__ = 'anyu'
19.1 Write a function to swap a number in place without temporary variables.

void swap(int &a, int &b){
    b = a - b;
    a = a - b;
    b = a + b;

    b= a-b
    a=a-b # a-(a-b)=b
    b=a+b # a+b=a

"""

def swap(a,b):
    b = a -b
    a = a - b
    b = a + b

    return a,b

print swap(2,4)

print swap(0,1)

print swap(-2,4)

