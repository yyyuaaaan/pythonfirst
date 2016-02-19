"""__author__ = 'anyu'
19.2 Design an algorithm to figure out if someone has won in a game of tic-tac-toe.
3**9,hashmap

19.3 Write an algorithm which computes the number of trailing zeros in n factorial.
写一个算法计算n的阶乘末尾0的个数。
首先，算出n的阶乘的结果再去计算末尾有多少个0这种方法是不可取的， 因为n的阶乘是一个非常大的数，分分种就会溢出。我们应当去分析， 是什么使n的阶乘结果末尾出现0。

n阶乘末尾的0来自因子5和2相乘，5*2=10。因此，我们只需要计算n的阶乘里， 有多少对5和2。注意到2出现的频率比5多，因此，我们只需要计算有多少个因子5即可。 我们可以列举一些例子，看看需要注意些什么：

5!, 包含1*5, 1个5
10!, 包含1*5,2*5, 2个5
15!, 包含1*5,2*5,3*5, 3个5
20!, 包含1*5,2*5,3*5,4*5, 4个5
25!, 包含1*5,2*5,3*5,4*5,5*5, 6个5
...
给定一个n，用n除以5，得到的是从1到n中包含1个5的数的个数；然后用n除以5去更新n， 相当于把每一个包含5的数中的因子5取出来一个。然后继续同样的操作，让n除以5， 将得到此时仍包含有5的数的个数，依次类推。最后把计算出来的个数相加即可。 比如计算25的阶乘中末尾有几个0， 先用25除以5得到5，表示我们从5,10,15,20,25中各拿一个因子5出来，总共拿了5个。 更新n=25/5=5，再用n除以5得到1，表示我们从25中拿出另一个因子5， 其它的在第一次除以5后就不再包含因子5了。
int NumZeros(int n){
    if(n < 0) return -1;
    int num = 0;
    while((n /= 5) > 0){
        num += n;
    }
    return num;
}

19.4 Write a method which finds the maximum of two numbers. You should not use if-else or any other comparison operator.
If (a - b) < 0, 令k = 1; else, 令k = 0. return a - k * (a - b).
令z = a - b. 令k是z的最高位，return a - k * z.
当a大于b的时候，a-b为正数，最高位为0，返回的a-k*z = a；当a小于b的时候， a-b为负数，最高位为1，返回的a-k*z = b。可以正确返回两数中较大的。

19.5 The Game of Master Mind is played as follows:
The computer has four slots containing balls that are red ®, yellow (Y), green (G) or blue (B). For example, the computer might have RGGB (e.g., Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue). You, the user, are trying to guess the solution. You might, for example, guess YRGB. When you guess the correct color for the correct slot, you get a “hit”. If you guess a color that exists but is in the wrong slot, you get a “pseudo-hit”. For example, the guess YRGB has 2 hits and one pseudo hit. For each guess, you are told the number of hits and pseudo-hits. Write a method that, given a guess and a solution, returns the number of hits and pseudo hits.
这个问题十分直观，但有一个地方需要去向面试官明确一下题意。关于pseudo-hits的定义， 猜对颜色但位置没对，得到一个pseudo-hit，这里是否可以包含重复？举个例子， 比如真实排列是：RYGB，猜测是：YRRR。那么hits很明显为0了。pseudo-hits呢？ 猜测中Y对应真实排列中的Y，得到一个pseudo-hits。猜测中有3个R， 而真实排列中只有一个，那这里应该认为得到1个pseudo-hits还是3个？ CTCI书认为是3个，想必理由是猜测中的3个R都满足：出现在真实排列中，位置不正确。 所以算3个。但我认为，这里算1个比较合理，真实排列中的R只和猜测中的一个R配对， 剩余的没有配对，不算。弄清题意后，代码就不难写出了。

19.8 Design a method to find the frequency of occurrences of any given word in a book.
这道题目和19.2是一个思路。如果只需要查询一次， 那就直接做；如果要多次查询，而且要查询各种不同的单词，那就先预处理一遍， 接下来就只需要用O(1)的时间进行查询。
只查询一次
遍历这本书的每个单词，计算给定单词出现的次数。时间复杂度O(n)，我们无法继续优化它， 因为书中每个单词都需要访问一次。当然，如果我们假设书中的单词是均匀分布， 那我们就可以只统计前半本书某个单词出现的次数，然后乘以2； 或是只统计前四分之一本书某个单词出现的次数，然后乘以4。这样能计算出一个大概值。 当然，单词均匀分布这个假设太强了，一般是不成立的。
多次查询
如果我们要对一本书进行多次的查询，就可以遍历一次这本书的单词， 把它出现的次数存入哈希表中。查询的时候即可用O(1)的时间完成。

19.10 Write a method to generate a random number between 1 and 7, given a method that generates a random number between 1 and 5 (i.e., implement rand7() using rand5()).
7.11 Implement a method rand70 given randSQ- That is,given a method that generates a random number between 0 and 4 (inclusive), write a method that generates a random number between 0 and 6 (inclusive).
均匀分布公式不行，这里只有整数
上述计算说明Rand5是等概率地生成1,2,3,4,5的(1/5的概率)。从上面的分析中， 我们可以得到一个一般的结论，如果a > b，那么一定可以用Randa去实现Randb。其中， Randa表示等概率生成1到a的函数，Randb表示等概率生成1到b的函数。代码如下：
// a > b
int Randb(){
    int x = ~(1<<31); // max int
    while(x > b)
        x = Randa();
    return x;
}
对a<b,我们先给出一个组合，再来进行分析。组合如下：
5 * (Rand5() - 1) + Rand5()
Rand5产生1到5的数，减1就产生0到4的数，乘以5后可以产生的数是：0,5,10,15,20。 再加上第二个Rand5()产生的1,2,3,4,5。我们可以得到1到25， 而且每个数都只由一种组合得到，即上述代码可以等概率地生成1到25。OK， 到这基本上也就解决了。
int Rand7(){
    int x = ~(1<<31); // max int
    while(x > 21)
        x = 5 * (Rand5() - 1) + Rand5() // Rand25
    return x%7 + 1;
}

19.11 Design an algorithm to find all pairs of integers within an array which sum to a specified value.
时间复杂度O(n)的解法
我们可以用一个哈希表或数组或bitmap(后两者要求数组中的整数非负)来保存sum-x的值， 这样我们就只需要遍历数组两次即可找到和为指定值的整数对。这种方法需要O(n) 的辅助空间。如果直接用数组或是bitmap来做，辅助空间的大小与数组中的最大整数相关， 常常导致大量空间浪费。比如原数组中有5个数：1亿，2亿，3亿，4亿，5亿。sum为5亿， 那么我们将bitmap中的sum-x位置1，即第4亿位，第3亿位，第2亿位，第1亿位，第0位置1. 而其它位置都浪费了。
如果使用哈希表，虽然不会有大量空间浪费，但要考虑冲突问题。
时间复杂度为O(nlogn)的解法
我们来考虑一种空间复杂度为O(1)，而且实现也很简单的算法。首先，将数组排序。 比如排序后得到的数组a是：-2 -1 0 3 5 6 7 9 13 14。然后使用low和high 两个下标指向数组的首尾元素。如果a[low]+a[high] > sum，那么说明a[high] 和数组中的任何其它一个数的和都一定大于sum(因为它和最小的a[low]相加都大于sum)。 因此，a[high]不会与数组中任何一个数相加得到sum，于是我们可以直接不要它， 即让high向前移动一位。同样的，如果a[low]+a[high] < sum，那么说明a[low] 和数组中的任何其它一个数的和都一定小于sum(因为它和最大的a[high]相加都小于sum)。 因此，我们也可以直接不要它，让low向前移动一位。如果a[low]+a[high]等于sum， 则输出。当low小于high时，不断地重复上面的操作即可。
void PrintPairSum(int a[], int n, int sum){
    if(a==NULL || n<2) return;

    sort(a, a+n);
    int low = 0, high = n-1;
    while(low < high){
        if(a[low]+a[high] > sum)
            --high;
        else if(a[low]+a[high] < sum)
            ++low;
        else{
            cout<<a[low]<<" "<<a[high]<<endl;
            ++low; --high;
        }

    }
}

We can approach this problem in two ways. The "preferred" solution depends on your preferences between time efficiency, space efficiency, and code complexity.
One easy and (time) efficient solution involves a hash map from integers to integers. This algorithm works by iterating through the array. On each element x, look up sum - x in the hash table and, if it exists, print (x, sum - x). Add x to the hash table, and go to the next element.

17.6 Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n,theentirearraywouldbesorted.Minimizen - m(that is, find the smallest such sequence).
left < middle < right
But, what we can do is shrink the left and right subsequences until the earlier conditions are met.

17.7 Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

This is not an especially challenging problem, but it is a somewhat tedious one. The key is to be organized in how you approach the problem—and to make sure you have good test cases.

We can think about converting a number like 19,323,984 as converting each of three 3-digit segments of the number, and inserting "thousands"and "millions" in between as appropriate.
convert(19,323,984)= convert(19)+"million"+ convert(323) +"thousand"+ convert(984)
if (number % 1900 != 0)
str = numToStringl00(number % 1000) + bigs[count] + ""+str;

The key in a problem like this is to make sure you consider all the special cases. There area lot of them.







"""
