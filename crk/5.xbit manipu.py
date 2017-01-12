"""
IN Python:
Bitwise operations only make sense for integers. Negative numbers are treated as their 2's complement
value (this assumes a sufficiently large number of bits that no overflow occurs during the operation).
The priorities of the binary bitwise operations are all lower than the numeric operations and higher
than the comparisons; the unary operation ~ has the same priority as the other unary numeric operations (+ and -).
x | y	bitwise or of x and
x ^ y	bitwise exclusive or of x and y x^y same is false, different is true
x & y	bitwise and of x and y
x << n	x shifted left by n bits	(1)(2)
x >> n	x shifted right by n bits	(1)(3)
~x	the bits of x inverted

You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all
bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j).
EXAMPLE:
Input: N = 100 0000 0000, M = 10101, i = 2, j = 6
Output: N = 10001010100
1. Clear thebits j through i in N
2. Shift M sothat it lines up with bits j through i
3. MergeMandN.
In a problem like this (and many bit manipulation problems), you should make sure to thoroughly test
your code. It's extremely easy to wind up with off-by-one errors.

signed
1111 1111	255 	−1 
1111 1110	254 	−2 
1000 0010	130 	−126 
1000 0001	129 	−127 
1000 0000	128 	−128
无论是有符号数还是无符号数，左移若干位后，原来最低位右边新出现的位全为0
一个有符号的正数，它的最高位为0，如果因为左移使得最高位为1，那么它变为负数， 而后无论怎样右移，它都还是负数。除非因为再次左移使最高位变为0，那么它变回正数。
int的最大值：~(1«31)，即0后面跟31个1
int的最小值：1«31，即1后面跟31个0
unsigned int最大值：~0，即32个1
unsigned int最小值：0
其它数据类型与int类似，只是位长不一样。

"""

def bitop(i,j,M,N):

    temp = 0b1
    #keep N[i:]
    bookkeeping=((temp<<i)-1)&N
    return ((N>>j)<<j) |bookkeeping | M<<j


print bin(bitop(2,6,0b10101,0b10000000000))

"""
set bit:&0001000;  getbit |111110
5.2
Given a real number between 0 and 7 (e.g., 0.72) that is passed in as a double, print the binary representation.
If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR."
整数部分通过不断地对2取余然后除以2来得到其二进制表示， 或是不断地和1按位与然后除以2得到其二进制表示。 小数部分则通过不断地乘以2然后与1比较
来得到其二进制表示。 小数部分转化为二进制，通过乘以2然后与1比较，大于等于1则该位为1，并且该值减去1； 否则该位为0。不断地通过这种操作最终能使
该小数部分的值变为0的，即可精确表示。

5.3
Given an integer, print the next smallest and next largest number that have the same number of 1 bits in their binary
 representation.
给定一个整数x，找出另外两个整数，这两个整数的二进制表示中1的个数和x相同， 其中一个是比x大的数中最小的，另一个是比x小的数中最大的。

对于这道题，我们先完成一个最朴素最直接的版本，以保证其正确性。 这个版本可以作为其它版本的验证工具。
什么方法是最直接的呢？function1:给定一个数x，计算出它的二进制表示中1的个数为num.（不断除1并count remainder 1））
然后x不断加1并用function1计算其二进制表示中1的个数，当它再次等于num时，
就找到了比x大且二进制表示中1的个数相同的最小的数。类似地， 可以找到比x小且二进制表示中1的个数相同的最大的数，只不过x变为不断减1而已。

5.4 Explain what the following code does: ((n & (n-1)) == 0).
这个比较简单，代码的作用是判断一个数是否为2的整数次幂。 100000 和11111

5.5
Write a function to determine the number of bits required to convert integer A to integer B.
这道题目也比较简单，从整数A变到整数B，所需要修改的就只是A和B二进制表示中不同的位， 先将A和B做异或，然后再统计结果的二进制表示中1的个数即可。

5.6
Write a program to swap odd and even bits in an integer with as few instructions as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc).
写程序交换一个整数二进制表示中的奇数位和偶数位，用尽可能少的代码实现。 (比如，第0位和第1位交换，第2位和第3位交换…)
这道题目比较简单。分别将这个整数的奇数位和偶数位提取出来，然后移位取或即可。

5.7
An array A[1…n] contains all the integers from 0 to n except for one number which is missing. In this problem,
we cannot access an entire integer in A with a single operation. The elements of A are represented in binary, and
the only operation we can use to access them is “fetch the jth bit of A[i]”, which takes constant time. Write code to
find the missing integer. Can you do it in O(n) time?
首先，在这个问题中，明确我们唯一能使用的操作是fetch(a, i, j)即： 取得a[i]中的第j位。它是提供给我们的操作，怎么实现的不用去理它，
而我们要利用它来解决这个问题，并且在我们的程序中，不能使用a[i]这样的操作。

如果我们不能直接使用a[i]，那么我们能利用fetch函数来获得a[i]吗？回答是可以。 数组a中每个元素是一个整型数，
所以只要每次取出32位，再计算出它的值即可。
我们已经通过get(a, i)来取得a[i]的值了，这样一来，我们只需要开一个bool数组， 把出现过的整数标记为true，即可找出丢失的那个整数。





"""