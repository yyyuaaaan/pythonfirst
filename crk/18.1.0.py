"""__author__ = 'anyu'"""
"""
20.1 Write a function that adds two numbers. You should not use + or any arithmetic operators.
由于我们不能使用任何算术运算符，因此可供我们使用的就只有位运算符了。
int Add2(int a, int b){
    if(b == 0) return a;
    int sum = a ^ b; // 各位相加，不计进位
    int carry = (a & b) << 1; // 记下进位
    return Add2(sum, carry); // 求sum和carry的和
}

20.2 Write a method to shuffle a deck of cards. It must be a perfect shuffle - in other words, each 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.

这是一道非常有名的面试题，及非常有名的算法——随机洗牌算法。
最直观的思路是什么？很简单，每次从牌堆中随机地拿一张出来。那么， 第一次拿有52种可能，拿完后剩下51张；第二次拿有51种可能，第三次拿有50种可能， …，一直这样随机地拿下去直到拿完最后1张，我们就从52!种可能中取出了一种排列， 这个排列对应的概率是1/(52!)，正好是题目所要求的。
接下来的问题是，如何写代码去实现上面的算法？假设扑克牌是一个52维的数组cards， 我们要做的就是从这个数组中随机取一个元素，然后在剩下的元素里再随机取一个元素… 这里涉及到一个问题，就是每次取完元素后，我们就不会让这个元素参与下一次的选取。 这个要怎么做呢。
我们先假设一个5维数组：1，2，3，4，5。如果第1次随机取到的数是4， 那么我们希望参与第2次随机选取的只有1，2，3，5。既然4已经不用， 我们可以把它和1交换，第2次就只需要从后面4位(2,3,1,5)中随机选取即可。同理， 第2次随机选取的元素和数组中第2个元素交换，然后再从后面3个元素中随机选取元素， 依次类推。

#random.randint(a, b)
#Return a random integer N such that a <= N <= b.
import random
deck = [None]*52
for i in range(52) # 0..51:
    j = random.randint(i,51) 产生i到n-1间的随机数
    deck[i], deck[j] = deck[j], deck[i]

>>> import random
>>> deck = range(1,53)
>>> random.shuffle(deck)
>>> deck

20.3 Write a method to randomly generate a set of m integers from an array of size n. Each element must have equal probability of being chosen.
这道题目和随机洗牌问题类似，只需要随机选取1个元素， 然后在剩下的元素里面随机选取下一个元素，不断这样操作即可。
这样做能保证每个元素选中的概率一样吗？也就是选中每个元素的概率都是1/n？ 答案是YES，让我们来做一下简单的计算。
选第1个元素：在n个中随机选，因此概率为1/n
选第2个元素：在剩下的n-1个中随机选：1/(n-1)，由于第1次没有选中它， 而是在另外n-1个中选：(n-1)/n，因此概率为：(n-1)/n * 1/(n-1) = 1/n
选第3个元素：同上：(n-1)/n * (n-2)/(n-1) * 1/(n-2) = 1/n
。。。
因此，按照这种方法选取k个元素，每个元素都是以1/n的概率被选出来的。代码如下： 选出的m个数放到数组前m个位置。

def pickmrandomly()
M = [None]*m
for i in range(m):
    j = random.randint(i,n-1):
    M[i], M[j] = M[j], M[i]

20.4 Write a method to count the number of 2s between 0 and n.
最简单直观的方法就是对于0到n之间的数，一个个地去统计2在它们上出现的个数， 然后累加起来即可。求2在某个数上出现的次数需要O(logn)的时间，一共有n个数， 所以共需要O(nlogn)的时间。
int Count2(int n){
    int count = 0;
    while(n > 0){
        if(n%10 == 2)
            ++count;
        n /= 10;
    }
    return count;
}

int Count2s1(int n){
    int count = 0;
    for(int i=0; i<=n; ++i)
        count += Count2(i);
    return count;

}
上述方法最大的问题就是效率，当n非常大时，就需要很长的运行时间。 想要提高效率，就要避开暴力法，从数字中找出规律。对于这道题， 《编程之美》已经给出了很漂亮的解法，这里再简述一下。 太烦

20.5 You have a large text file containing words. Given any two words, find the shortest distance (in terms of number of words) between them in the file. Can you make the searching operation in O(1) time? What about the space complexity for your solution?
If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution?
首先，我们遇到的第一个问题是：是否要考虑顺序？我们求的是is和name间的距离， 那么文本中先出现name再出现is的情况要不要算进来。这一点是要和面试官进行交流确认的。 这里我们假设不考虑顺序，并且认为本文中只有单词，没有标点。 为了进一步简化问题，我们可以用一个字符串数组来保存单词， 接下来考虑如何计算两个单词间的最短距离。
最直观的一个解法是，遍历单词数组，遇到is或name就更新它们的位置， 然后计算is和name之间的距离，如果这个距离小于之前的最小距离，则更新这个最小距离。 看图示：
What is your name My name is Hawstein
0    1  2    3    4  5    6  7
                  p
p表示遍历的当前位置。此时已经经过了前面的一个is和name，is位置为1，name位置为3， 最小距离min=3-1=2。当p移动到下一个单词，发现是name，则更新name的位置为5， 减去is的位置1得到4，并不小于min，不更新，继续。当p移动到is，更新is的位置为6， 减去name的位置5，得到距离为1，小于min，更新min=1。p之后一直移动到末尾， 没遇到is或name，不再更新。最后返回最小值min。时间复杂度O(n)，空间复杂度O(1)。
题目要求在O(1)的时间内返回两个单词的最短距离，上述代码肯定是无法满足要求的。 那要怎么做呢？只能用哈希表做预处理了，空间换时间。

方法二
预处理阶段把文本中任意两个单词间的最小距离计算出来， key是两个单词连接后的哈希值，value保存的就是最小距离。 查找阶段就只需要把两个单词连接求其哈希值，然后直接返回其对应的value即可。 查找两个单词的最小距离时间复杂度O(1)。需要O(n2 )的时间来做预处理。

由于我们是不考虑顺序的，因此做两个单词的连接时，不能直接连接， 这样会导致is和name连接后是isname，而name和is连接后nameis， 它们的哈希值不一样，这并不是我们想要的。因此，在做两个单词的连接时， 我们可以让第一个字符较小的单词放在前面(反正定义一个规则来保证连接的唯一性即可)。 比如对于name和is，由于在字典序中，i<n，所以连接是isname。

还是用上面的例子，预处理后得到：(哈希值是随便写的数字，示意用)

单词连接      哈希值   最小距离
(isWhat)     8       1
...          ...     ...
(isname)     12      1
...          ...     ...
(isMy)       33      2
...          ...     ...
这样当我要求is和name之间的最小距离时，就只需要先连接它们得到isname， 然后用哈希函数求出isname的哈希值12，然后直接返回它对应的最小距离即可。

如果有冲突怎么办？即两个不同的字符串映射到同一个哈希值，我们可以用链地址法， 把冲突的连接字符串链接起来，这样每个结点就需要保存连接字符及其对应的最小距离。 比如对于上面的例子，假设isname和isMy的哈希值相同，我们可以按如下所示去做：

哈希值   最小距离
8       (isWhat,1)
...     ...
12      (isname,1) -> (isMy,2)
...     ...
这样一来，当我们求得一个连接字符串str的哈希值是12， 就依次去与其后面的结点做比较。如果str等于isname，返回1；否则，移动到下一个结点， 继续比较。如果str等于isMy，返回2。

20.6 Describe an algorithm to find the largest 1 million numbers in 1 billion numbers. Assume that the computer memory can hold all one billion numbers.
这是一道经典的面试题，一般有以下几种解法：
排序法
最直观的方法就是将数组从大到小排序，然后取前1百万个数即可。时间复杂度O(nlogn)。

最小堆
利用最小堆来维护最大的1百万个数，堆顶元素是这1百万个数中最小的。 遍历剩下的元素，当某一元素大于堆顶元素，则用该元素替换堆顶元素， 然后调整堆结构，使其仍为最小堆。当遍历完所有10亿个数后， 堆中维护的就是最大的1百万个数。在n个数中查找最大的k个数，该算法需要O(nlogk) 的时间。由于k一般要比n小得多，所以该算法比排序法要快。
该算法还有一个优点，就是便于处理大数据。比如说， 我们一般需要在非常多的数中找到最大(最小)的k个数，这个k一般比较小， 而n却可能大得无法一次性载入内存。这时候我们就可以在内存中维护一个k 个元素的最小(最大)堆，然后把数据分多次从磁盘读入内存进行处理。

20.7 Write a program to find the longest word made of other words in a list of words.
EXAMPLE Input: test, tester, testertest, testing, testingtester Output: testingtester
题目说要找最长单词，所以你的眼睛自然会去寻找那些长单词，至少你不会从bat 开始找起，对吧。找到最长的单词是testbattingcat， 下一步去看它是否可以由其它单词组成。我们发现test是testbattingcat的一部分， bat也是它的一部分，然后呢？剩下的tingcat不能由其它单词构成。不过， 我们可以用test，batti，ngcat来组成它。所以， 它就是我们要找的可以由其它单词组成的最长单词。
把上面的思考过程转换成算法，可以描述如下：
按单词的长度从大到小排序。(先寻找最长的单词)
不断地取单词的前缀s，当s存在于单词数组中，递归调用该函数， 判断剩余串是否可以由其它单词组成。如果可以，返回true。
对于上面的例子testbattingcat，我们通过不断取前缀：t不在数组中，te不在数组中， tes不在数组中，test在数组中；递归调用去处理剩余串battingcat，b不在数组中， ba不在数组中，bat在数组中；递归调用去处理剩余串tingcat， 发现它所有的前缀都不存在于数组中，退递归来到处理battingcat那一层。 接着上次的bat继续处理：batt不在数组中，batti在数组中；递归调用去处理剩余串 ngcat，n，ng，ngc，ngca都不在数组中，ngcat存在数组中。递归调用处理剩余串， 发现剩余串为空，返回真。
上述代码将单词存放在哈希表中，以得到O(1)的查找时间。排序需要用O(nlogn)的时间， 判断某个单词是否可以由其它单词组成平均需要O(d)的时间(d为单词长度)， 总共有n个单词，需要O(nd)的时间。所以时间复杂度为：O(nlogn + nd)。 n比较小时，时间复杂度可以认为是O(nd)；n比较大时，时间复杂度可以认为是O(nlogn)。

20.8 Given a string s and an array of smaller strings T, design a method to search s for each small string in T.
给一个字符串S和一个字符串数组T(T中的字符串要比S短许多)，设计一个算法， 在字符串S中查找T中的字符串。
XXXfix suffix, trie, prefix leetcode没有，evernote也没有，舍弃
我们把S称为目标串，T中的字符串称为模式串。设目标串S的长度为m，模式串的平均长度为 n，共有k个模式串。如果我们用KMP算法(或BM算法)去处理每个模式串， 判断模式串是否在目标串中出现， 匹配一个模式串和目标串的时间为O(m+n)，所以总时间复杂度为：O(k(m+n))。 一般实际应用中，目标串往往是一段文本，一篇文章，甚至是一个基因库， 而模式串则是一些较短的字符串，也就是m一般要远大于n。 这时候如果我们要匹配的模式串非常多(即k非常大)，那么我们使用上述算法就会非常慢。 这也是为什么KMP或BM一般只用于单模式匹配，而不用于多模式匹配。
那么有哪些算法可以解决多模式匹配问题呢？貌似还挺多的，Trie树，AC自动机，WM算法， 后缀树等等。我们先从简单的Trie树入手来解决这个问题。
Trie树，又称为字典树，单词查找树或前缀树，是一种用于快速检索的多叉树结构。 比如英文字母的字典树是一个26叉树，数字的字典树是一个10叉树。
Trie树可以利用字符串的公共前缀来节约存储空间，这也是为什么它被叫前缀树。
回到我们的题目，现在要在字符串S中查找T中的字符串是否出现(或查找它们出现的位置)， 这要怎么和Trie扯上关系呢？
假设字符串S = “abcd"，那么它的所有后缀是：
abcd
bcd
cd
d
我们发现，如果一个串t是S的子串，那么t一定是S某个后缀的前缀。比如t = bc， 那么它是后缀bcd的前缀；又比如说t = c，那么它是后缀cd的前缀。
因此，我们只需要将字符串S的所有后缀构成一棵Trie树(后缀Trie)， 然后查询模式串是否在该Trie树中出现即可。如果模式串t的长度为n， 那么我们从根结点向下匹配，可以用O(n)的时间得出t是否为S的子串。
后缀Trie的查找效率很优秀，如果你要查找一个长度为n的字符串，只需要O(n)的时间， 比较次数就是字符串的长度，相当给力。 但是，构造字符串S的后缀Trie却需要O(m2 )的时间， (m为S的长度)，及O(m2 )的空间。

20.9 Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.
方法一
最简单直观的方法是用一个足够大的数组A来维护这些数，使其按升序排列。 这样一来，可以用O(1)的时间找到中位数。下面是图示：
这种方法插入一个新来的元素需要O(n)的时间， 需要在原来有序的数组中找到一个合适的位置插入它，并把比它大的元素都向后移动1位。
方法二
用一个最大堆(或最小堆)来维护这些数。那么插入一个新元素需要O(logn)的时间， 比方法一要好。但取中位数需要先排序，时间复杂度O(nlogn)。
方法三
使用堆来维护数据是个不错的选择，因为插入一个新元素只需要O(logn)的时间， 但取中位数比较耗时，时间主要花在排序上。有没方法可以不排序呢？ 我们知道，中位数是一个有序序列中排在中间的数，它左右两边的数相当。 从方法一的示意图可以看出，当数组大小n为奇数时，中位数就是有序序列中正中间那个数， 如果n为偶数，它是中间两个数的平均数。它只和序列中间的一个或两个数有关， 和其它的元素无关。那么，如果我用一个最大堆维护中位数左边的数(包含它)， 用一个最小堆维护中位数右边的数。当n为偶数时，我只需要把左边的数最大那个， 和右边的数最小那个相加除以2即可。左边的最大数即最大堆的堆顶元素， 右边最小数即最小堆的堆顶元素。当n为奇数时，如果最大堆的元素比最小堆的元素多1， 则最大堆的堆顶元素是中位数；如果最小堆的元素比最大堆的元素多1， 则最小堆的堆顶元素是中位数。在插入新元素的时候，我们只要维护两个堆， 使其堆中元素的数量差别不超过1即可。
这样一来，插入新元素还是O(logn)的时间，而取中位数只需要O(1)的时间， 要优于方法一和方法二。

20.11 Imagine you have a square matrix, where each cell is filled with either black or white. Design an algorithm to find the maximum subsquare such that all four borders are filled with black pixels.
有一个正方形矩阵，里面的每一个小格子要么被涂上黑色要么被涂上白色。 设计算法，找到四条边都是黑色格子的最大子正方形。
暴力法，从左到右，从上到下遍历格子，将它作为子正方形左上角的点。 固定了子正方形左上角的点，我们只需要知道边长，就能把子正方形确定下来。 我们按边长从大到小开始，去检查每一个子正方形的四条边是否都为黑色格子。 如果是，则记下当前最大的边长值。将子正方形左上角的点移动到下一行(即向下移动一格)， 进入下一轮循环。
Pre-Processing Solution:O(N3)
A large part of the slowness of the "simple" solution above is due to the fact we have to do 0(N) work each time we want to check a potential square. By doing some pre- processing, we can cut down the time of isSquare to 0(1). The time of the whole algorithm is reduced to 0(N3). Hashtable

20.12 Given an NxN matrix of positive and negative integers, write code to find the submatrix with the largest possible sum.
暴力法，时间复杂度O(n6 )
最简单粗暴的方法就是枚举所有的子矩阵，求和，然后找出最大值。 枚举子矩阵一共有C(n, 2)*C(n, 2)个(水平方向选两条边，垂直方向选两条边)， 时间复杂度O(n4 )，求子矩阵中元素的和需要O(n2 )的时间。 因此总的时间复杂度为O(n6 )。
部分和预处理，时间复杂度降到O(n4 )
上面的方法需要O(n2 )去计算子矩阵中元素的和。 这一部分我们可以在预处理的时候求出部分和，在使用的时候就只需要O(1) 的时间来得到子矩阵中元素的和。

18.13 Given a list of millions of words, design an algorithm to create the largest possible rectangle of letters such that every row forms a word (reading left to right) and every column forms a word (reading top to bottom). The words need not be chosen consecutively from the list, but all rows must be the same length and all columns must be the same height.
Many problems involving a dictionary can be solved by doing some pre-processing. hashtable?

"""
