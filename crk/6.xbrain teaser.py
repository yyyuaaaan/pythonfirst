
"""
6.1 You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams.
Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once.

Sometimes, tricky constraints can be a clue.
 In fact, we know we must weigh pills from at least 19 bottles at the same time.
 关键：对每个瓶子要单独标记，称一次才可能称出来，所以第一个瓶子取1片，第二个2片，这样多了多少个0.1克，就是几号瓶子。
Take one pill from Bottle #1, two pills from Bottle #2, three pills from Bottle #3, and so on. Weigh this mix of pills,
any grams more than (1+2+..+20)=210 must come the extra 0.1 grams pills.

6.1
Add arithmetic operators (plus, minus, times, divide) to make the following expression true: 3 1 3 6 = 8.
You can use any parentheses you’d like.
简单题，就不翻译了。答案：(3 + 1) / (3 / 6) = 8.

6.2
There is an 8x8 chess board in which two diagonally opposite corners have been cut off. You are given 31 dominos, and
 a single domino can cover exactly two squares.Can you use the 31 dominos to cover the entire board? Prove your
 answer (by providing an example, or showing why it’s impossible).关键就是棋盘的着色
有一个8x8的国际象棋棋盘，对角线两端的方格被去掉了。你有31个多米诺骨牌， 每个骨牌能覆盖棋盘上两个方格。你能用31个多米诺骨牌覆盖整个棋盘吗
( 不包含去掉的2个方格)。如果能，请给出覆盖方案；如果不能，请说明为什么。
这是一道非常经典的问题，详情见：Mutilated chessboard problem。 这道题目的答案是不能。为什么呢？先让我们来看看下面的图。

如果不去掉对角的两个方格，我们可以用32个多米诺骨牌把棋盘完全覆盖， 每个骨牌覆盖两个方格，共覆盖了32*2=64个方格。并且， 每个骨牌正好覆盖一个红色方格和一个黄色方格。也就是，我每往棋盘上放一个骨牌， 棋盘上就少掉一个红色方格和一个黄色方格，这是一个必然事件。那么， 当对角的两个黄色方格被去掉后，剩下32个红色方格和30个黄色方格。 我每放一个骨牌还是会覆盖掉一个红色方格和一个黄色方格，最后的情况是， 剩下2个红色方格。从棋盘上可以看出，任意两个红色方格都无法用一个骨牌覆盖， 因此，这道题目的答案是不能用31个多米诺骨牌将去掉两个角的棋盘覆盖。

这道题目的关键就是棋盘的着色，如果你画一个8x8的白色棋盘， 也许会很茫然的不知如何下手。这道题目推广一下，可以得到以下结论： 从棋盘上任意去掉两个方格，如果去掉方格的颜色是一样的，那么， 我们无法用31个多米诺骨牌将剩余的方格覆盖；如果去掉的方格的颜色是不一样的， 那么，我们一定可以用31个多米诺骨牌将剩余的方格覆盖。

6.3
You have a five quart jug and a three quart jug, and an unlimited supply of water(but no measuring cups). How would you come up with exactly four quarts of water? NOTE: The jugs are oddly shaped, such that filling up exactly ‘half’ of the jug would be impossible.
大意就是：你有两个瓶子，一个可以装5升水，一个可以装3升水， 怎样利用这两个瓶子量出4升水来。
简单题。先装满5升水，倒到3升的瓶子里，5升的瓶子中剩余2升水；再把3升的瓶子倒空， 把5升瓶子里的2升水倒到3升的瓶子里，3升瓶子还可装1升水；最后装潢5升水， 往3升瓶子里倒，当3升瓶子满时，5升瓶子里就正好装了4升水。

6.4
A bunch of men are on an island. A genie comes down and gathers everyone together and places a magical hat on some people’s heads ( i.e., at least one person has a hat). The hat is magical: it can be seen by other people, but not by the wearer of the hat himself. To remove the hat, those (and only those who have a hat) must dunk themselves underwater at exactly midnight. If there are n people and c hats, how long does it take the men to remove the hats? The men cannot tell each other (in any way) that they have a hat.
FOLLOW UP
Prove that your solution is correct.
译文：
在一个岛上有一群人，他们中有些人的头上被戴上了一顶神奇的帽子(至少有一人戴了帽子)， 这顶帽子别人看得到，但戴帽子的人自己看不到。想要去掉这顶帽子， 需要戴着帽子的本人在正好午夜的时候，把自己泡在水里。如果有n个人，c个帽子， 需要多长的时间才能把所有的帽子都摘除。注： 这群人不能相互告诉对方他们的头上是否有帽子。
解答6.4
也是被问烂的智力题之一了吧。与它类似的一个题目是：村庄里有几条病狗？ 这类题目的一个前提是题中的人都要非常聪明，懂推理。不然，题目就没有任何意义了。 这类题目都是从一个条件的最基本情况出发，然后得出规律。比如这道题， 假如只有一个帽子，那么戴着帽子的那个人出去一看，另外n-1个人都没有帽子， 而题目已经说了，至少有一个人是戴着帽子的，所以可以推断唯一一个戴着帽子的就是自己， 于是他会在第1天的午夜泡到水里，去掉头上的帽子。如果有2个帽子， 比如说是A和B戴着，A第1天发现B是戴着帽子的，而A又不知道一共有多少个帽子， 所以他无法判断自己头上是否戴了帽子，因此A第1天什么也不做。同理，B也一样。 到了第二天，A发现B还戴着他的帽子，这就说明了至少要有2顶帽子。否则如果只有一顶， B能推理出来，并且在第一天午夜就去掉它了。如果至少有2顶，B已经戴了一顶， 那么另一顶就在自己(A)头上了，所以A在第2天的午夜去掉了帽子。同理， B也做出了同样的推理，在第2天午夜去掉了帽子。
从以上的分析我们马上可以得出，如果有c个帽子， 那么需要c天的时间才能把所有的帽子去掉，而且这c个人都是在第c天的午夜才摘除帽子的。

题意：
有一个村庄有n户人家，每户人家养了一条狗。有一天，村民接到通知，村庄内有病狗。于是大家都把狗带给别的村民观察。已知每户居民都可以观察到其他居
民的狗，并准确判断哪些狗是病狗，但是却不能正确判断自己家的狗是否得病。但是，村民之间相互无法沟通。这些村民如果断定自家的狗是病狗，就会在当天开枪将其击毙。每户村民都是极其聪明的。到了第k天，村庄里响起枪声。请问有多少条狗被击毙？
1、村庄内有病狗，说明病狗数量设为x>=1;
2、假设x=1,病狗主人在观察其它所有村民的狗以后未发现病狗后，确定自己家的狗为病狗，就会在当天开枪将其击毙。所以k = 1;
3、假设x=2,第一天病狗主人a和b都发现有1条病狗，但因不确定自己家的狗是否得病，故第一天未杀死自己家的狗，而到了第2天，可以确定x!=1;而除了自己的狗以外，只发现1只病狗，所以自己家的狗肯定是病狗，所以k=2;
4、同理，x = C，如果病狗主人在观察到的病狗数量为C-1，如果在C-1天里未发现有村民杀病狗，就可以确定自己家的狗为病狗，并且在第C天杀死自己家的狗。所以C=K，所以X=K。

6.5 DP
There is a building of 100 floors. If an egg drops from the Nth floor or above it will break. If it’s dropped from any floor below, it will not break. You’re given 2 eggs. Find N, while minimizing the number of drops for the worst case.

6.6
There are one hundred closed lockers in a hallway. A man begins by opening all one hundred lockers. Next, he closes every second locker. Then he goes to every third locker and closes it if it is open or opens it if it is closed (e.g., he toggles every third locker). After his one hundredth pass in the hallway, in which he toggles only locker number one hundred, how many lockers are open?
在过道上有100把上了锁的锁头。有一个人，第一次操作把这100把锁都打开了； 第二次操作，每隔1个锁他就把锁给锁上(即把编号2，4，6…100的锁锁上)。 第三次操作，每隔2个锁他就改变锁的状态，即如果原本是开着的，他就锁上； 原本是锁着的，他就给打开。(操作对象是编号为3,6,9…99的锁)。 当他做完第100次操作后(即只对编号为100的锁操作)，打开着的锁有几把？

简单题。每次就改变一些锁的状态。第1把锁只会在第1次操作时被改变状态， 第2把锁会在第1次及第2次操作时被改变状态，假设能被i整除的数有a,b,c， (包含1和它本身)，那么第i把锁会被改变3次，分别是在第a，b，c次操作的时候。 这样一来，对于第i把锁，如果能被i整除的数有奇数个， 那么它最后的状态一定打开的，否则则是关闭的。问题就转换为1到100的数中， 哪些数能整除的数的个数有奇数个。而，一个数i如果能整除a， 那么它也可以整除i/a，这样一来，一个数能整除的数总是成对出现， 为了使个数是奇数，这里面一定要有一对是相等的，即a = i/a，也就是：i = a2， 所以，最后开着的锁就是编号为完全平方数的锁，即： 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
一共有10把锁是打开着的。
