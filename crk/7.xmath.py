""""""
"""
7.1 You have a basketball hoop and someone says that you can play one of two games.
Game 1: You get one shot to make the hoop.
Game 2: You get three shots and you have to make two of three shots.
If p is the probability of making a particular shot, for which values of p should you pick one game or the other?
命中率是p，那么对于游戏1，赢的概率是p。对于游戏2，至少进2个球才算赢， 那么赢的概率为：
C(2,3)p^2(1-p) + p^3 = 3p^2 - 2p^3
哪个游戏赢的概率大我们就选哪个游戏，所以当
p > 3p^2 - 2p^3  -->  p < 0.5
我们选游戏1。当p > 0.5时，我们选游戏2。当p = 0.5时，选哪个都可以，赢的概率相等。


7.2 There are three ants on different vertices of a triangle. What is the probability of collision (between any two or all of them) if they start walking on the sides of the triangle? Assume that each ant randomly picks a direction, with either direction being equally likely to be chosen,and that they walk at the same speed.
Similarly, find the probability of collision with n ants on an n-vertex polygon.
首先，题目中没有提到蚂蚁运动的速度，所以认为它们的速度一样， 不会发生一只蚂蚁追上另一只蚂蚁的情况(面试时可以向面试官确认一下)。 对于任何1只蚂蚁，它有2条边可以选择来走。不会发生冲突的情况是， 所有的蚂蚁都顺时针走或是逆时针走，剩下的情况都是会冲突的。所以，冲突的概率为：
p = 1 - 2 * (1/2)^3 = 3/4
对于n只蚂蚁在n边形上，道理是一样的：
p = 1 - 2 * (1/2)^n = 1 - 1/2^(n-1)

7.3 Given two lines on a Cartesian plane, determine whether the two lines would intersect.
这道题目给出的条件非常有限。首先，我们要考虑一些边界条件，比如直线重合， 重合的话是否算相交(假设我们把重合算作是相交)。还有当直线垂直于x轴时， 此时直线的斜率不存在，我们如果用斜率和直线在y轴上的截距来表示直线的话， 这种情况怎么表示？接着是其它一般的情况，斜率不相等时，两直线相交， 但我们不能假设斜率是整数，如果是浮点数，表示两个数不相等是让它们作差， 然后它们的差大于一个足够小的数epsilon(一般为0.000001)。

7.4 Write methods to implement the multiply, subtract, and divide operations for integers. Useonly the add operator.
首先对于这道题目，我们要和面试官确认一下，是不是只针对整数来讨论。 你自己在心里看到这道题目，也要大概估计到应该只在整数范围内考察。否则， 要你只用加法实现个浮点数相乘或是相除，恐怕就不太好办了。

对于乘法，比如a*b(a>0, b>0)，可以视为a个b相加，或是b个a相加。 如果a，b中有负数呢？我们可以先将它们取绝对值相乘，然后再根据同号相乘为正， 异号相乘为负给结果加上符号。其中，我们还可以做一点小优化， 即如果a<b，就求a个b相加；如果a>b，就求b个a相加。这样可以加法运算次数。

对于减法，a-b，我们只需要转变为a+(-b)即可。

对于除法，a/b，首先我们要考虑的是b不能为0.当b等于0时，抛出异常或返回无穷大(程序 中定义的一个值)。与乘法相同，我们都先对a和b取绝对值，然后不断地从a中减去b， 相应的商数加1。直到a已经不够给b减了，再根据a和b的符号决定是否给商数加上负号即可。
All (good) interview problems can be approached in a logical, methodical way!
The interviewer is looking for this sort of logical work-your-way-through-it approach.
This is a great problem to demonstrate your ability to write clean code—specifically, to show your ability to reuse code.
Be careful about making assumptions while coding. Don't assume that the numbers are all positive or that a is bigger than b.

7.5 Given two squares on a two-dimensional plane, find a line that would cut these two squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis.
一条直线只要过正方形的中心，就一定会将它分为面积相等的两半。(矩形也一样) 那么，我们只要作一条过这两个正方形中心点的直线， 即可同时把这两个正方形都分为面积相等的两半。
The main goal of this problem is to see how careful you are about coding. It's easy to glance over the special cases (e.g., the two squares having the same middle). You should make a list of these special cases before you start the problem and make sure to handle them appropriately. This is a question that requires careful and thorough testing.

7.6 Given a two-dimensional graph with points on it, find a line which passes the most number of points.
貌似这是一道Goolge面试题目，好想不好做。我们可以每两个点计算出一条直线， 然后将它们放入以直线为键，数量为值的hash map中，以此来求经过点数最多的直线。 这样一说，好像OK了，但是这样吗？首先，键值相等就是一个问题。 假如我们用斜截式表达直线，由于斜率和截距都是浮点数， 那么相等的概念在这里就不能理解为精确的相等，而是两数相差小于一个非常小的数。 可是hash map默认可不管，它就认为它们两个是不同的键。导致的结果是什么呢？ 就是平面上任何两个点之间形成的直线都不是同一条直线。

c++的STL标准里没有hash map，于是我用map来模拟，并写一个hashcode 函数将一条直线转换为一个整型码。 这样当两直线的斜率和截距相差都小于epsilon时，都将被映射到一个整数， 从而认为它们是一条直线。
 The problem is that floating point numbers cannot always be represented accurately in binary. We resolve this by checking if two floating point numbers arewithin an epsilon value of each other.
 .Then, to retrieve all lines that are potentially equal, we will search the hashtable at three spots: flooredSlope, f looredSlope - epsilon, and f looredSlope + epsilon. This will ensure that we've checked out all lines that might be equal.

7.7 Design an algorithm to find the kth number such that the only prime factors are 3,5, and 7.
设计算法，找到质因数只有3，5或7的第k个数。
首先，我们可以将满足条件的前几个数列出来，以此寻找解题思路。

When you get this question, do your best to solve it—even though it's really difficult. You can start with a brute force approach (challenging, but not quite as tricky), and then you can start trying to optimize it. Or, try to find a pattern in the numbers.
Chances are that your interviewer will help you along when you get stuck. Whatever you do, don't give up! Think out loud, wonder out loud, and explain your thought process. Your interviewer will probably jump in to guide you.
Remember, perfection on this problem is not expected. Your performance isevaluated in comparison to other candidates. Everyone struggles on a tricky problem.
首先，我们可以将满足条件的前几个数列出来，以此寻找解题思路。

一种简单的思路就是对于已经列出的数，我们依次去乘以3，5，7得到一组数 然后找出最小且还没有列出的数，加入到这个列表。然后重复上面的步骤： 乘以3，5，7，找出最小且还没有列出的数……这个方法的时间复杂度是O(n2 )。

这种思路存在一个问题，就是重复计算。比如对于上面那个表，我想计算下一个数， 那么我用3，5，7去乘以表中的每一个数，然后找出最小且没有用过的数。 可是像3*3,3*5,3*7,5*5,5*7等等都是已经计算过且已经用了的， 按照上面的算法就会不断地重复计算。那我们有没什么办法可以避免重复计算呢？ 那就是将已经计算出来的数保存好，并且保持它们有序。为了避免出现先用3乘以5， 然后又用5去乘以3的这种情况出现(这样会使我们维护的数中出现重复)， 我们可以用3个队列来维护这些数。第1个队列负责乘以3，第2个队列负责乘以5， 第3个队列负责乘以7。算法描述如下：

1. 初始化结果res=1和队列q3,q5,q7
2. 分别往q3,q5,q7插入1*3,1*5,1*7
3. 求出三个队列的队头元素中最小的那个x，更新结果res=x
4. 如果x在：
    q3中，那么从q3中移除x，并向q3，q5，q7插入3*x,5*x,7*x
    q5中，那么从q5中移除x，并向q5，q7插入5*x,7*x
    q7中，那么从q7中移除x，并向q7插入7*x
5. 重复步骤3－5，直到找到第k个满足条件的数


"""