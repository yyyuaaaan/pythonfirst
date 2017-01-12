""""""
"""
Explain the following terms: virtual memory, page fault, thrashing.
缺页中断一个页(Page)是一个固定容量的内存区块，是物理内存和外部存储(如硬盘等) 传输的单位。当一个程序访问一个映射到地址空间却实际并未加载到物理内存的页（page）时， 硬件向软件发出的一次中断（或异常）就是一个缺页中断或叫页错误（page fault）。
抖动在分页存储管理系统中，内存中只存放了那些经常使用的页面， 而其它页面则存放在外存中，当进程运行需要的内容不在内存时， 便启动磁盘读操作将所需内容调入内存，若内存中没有空闲物理块， 还需要将内存中的某页面置换出去。也就是说，系统需要不断地在内外存之间交换信息。 若在系统运行过程中，刚被淘汰出内存的页面，过后不久又要访问它， 需要再次将其调入。而该页面调入内存后不久又再次被淘汰出内存，然后又要访问它。 如此反复，使得系统把大部分时间用在了页面的调入/换出上， 而几乎不能完成任何有效的工作，这种现象称为抖动。
Write a program to find whether a machine is big endian or little endian.
 byte = 0x001,return byte[0]
Big-endian is the most common convention in data networking (including IPv6), hence its pseudo-synonym network byte order, and little-endian is popular (though not universal) among microprocessors in part due to Intel's significant historical influence on microprocessor designs.

12.1
If you were integrating a feed of end of day stock price information ( open, high, low,and closing price) for 5,000 companies, how would you do it? You are responsible for the development, rollout and ongoing monitoring and maintenance of the feed. Describe the different methods you considered and why you would recommend your approach. The feed is delivered once per trading day in a comma-separated format via an FTP site. The feed will be used by 1000 daily users in a web application.
假设我们有一些脚本在每日结束时通过FTP获取数据。我们把数据存储在哪？ 我们怎样存储数据有助于我们对数据进行分析？
方案一
将数据保存在文本文件中。这样子的话，管理和更新都非常麻烦，而且难以查询。 保存无组织的文本文件是一种非常低效的方法。
方案二
使用数据库。这将带来以下的好处：
数据的逻辑存储
提供了非常便捷的数据查询方式
例子：return all stocks having open > N AND closing price < M (返回开盘价大于N且收盘价小于M的所有股票)
优势：
使得维护更加简单
标准数据库提供了回滚，数据备份和安全保证等功能。我们不需要重复造轮子。
方案三
如果要求不是那么宽泛，我们只想做简单的分析和数据分发，那么XML是另一个很好的选择。 我们的数据有固定的格式和大小：公司名称，开盘价，最高价，最低价和收盘价。 XML看起来应当如下所示：
<root>
  <date value=“2008-10-12”>
    <company name=“foo”>
      <open>126.23</open>
      <high>130.27</high>
      <low>122.83</low>
      <closingPrice>127.30</closingPrice>
    </company>
    <company name=“bar”>
      <open>52.73</open>
      <high>60.27</high>
      <low>50.29</low>
      <closingPrice>54.91</closingPrice>
    </company>
  </date>
  <date value=“2008-10-11”> . . . </date>
</root>
优势：
便于数据分发。这就是为什么XML是共享及分发数据的一个标准模型。
我们有高效的解析器来提取出想要的数据
我们可以往XML文件中追加新数据
不足之处是数据查询比较麻烦(这点比不上数据库)。

12.2
How would you design the data structures for a very large social network (Facebook,LinkedIn, etc)? Describe how you would design an algorithm to show the connection, or path, between two people (e.g., Me -> Bob -> Susan -> Jason -> You).
方法：

首先，我们先不去考虑数据规模。先从简单的入手。

我们可以把每个人看作一个结点，如果两个人之间是朋友，则这两个结点间有一条边， 这样一来我们就可以构建出一个图。假设我们将“人”这个类设计如下：

class Person {
    Person[] friends;
    // Other info
}
如果要找到两个人之间的联系，即两个人之间间隔着哪些人。我们就从其中的一个人开始， 做广度优先搜索(BFS)。（做双向的BFS会更快）

但是。。。数据规模太大了！

如果我们去处理Orkut或是Facebook上的数据，单台机器根本无法完成这个任务。 因此，我们考虑用多台机器来处理这个问题。这样一来，Person这个类就需要修改了。 在Person类中，我们存储朋友的ID，然后按照以下方式找到朋友：

对于每个朋友id：int machine_index = lookupMachineForUserID(id);
转到标号为machine_index的机器去
Person friend = lookupFriend(machine_index);
对于这个问题，要考虑的优化和问题非常多，这里只列出一些。

优化：减少机器间的跳转次数

机器间的跳转是非常耗时的，因此我们不随机的跳转，而是进行批处理： 比如一个人，他其中的5个朋友在同一台机器上，那么跳转到那台机器后，一次性处理他们。

聪明地划分人与机器

由于同一国家的人更有可能是朋友，因此我们并不随机地把人分配到不同的机器上， 而是以国家，城市，州等进行划分。这样也可以减少机器间的跳转次数。

问题：广度优先搜索会标记已访问结点，对于这个问题，你怎么处理？

在这个问题中，有可能同时有许多人在搜索两人间的联系， 因此直接在原数据上做修改并不好。那怎么办呢？我们可以对每一个搜索， 使用一个哈希表来记录一个结点是否已经访问过。这样一来， 不同人的搜索之间就不会互相干扰。

其它问题

在真实的世界中，服务器有可能会出故障。你会怎么做？
你怎么利用缓存？
你是否一直搜索直到把图上的结点都遍历一次。如何决定什么时间停止搜索。
在真实世界中，你的朋友里，有一些人的朋友会更多。 那么通过他是否更有可能让你找到与特定某个人的联系。 你怎么利用这个数据来选择遍历的顺序。


12.3
Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in the file. Assume you have 1 GB of memory.
FOLLOW UP
What if you have only 10 MB of memory?
解答
4 * 10^9 * 4B = 16GB (大约值，因为不是按照2的幂来做单位换算)
这个明显无法一次性装入内存中。但是，如果我们用计算机中的一位来表示某个数出现与否， 就可以减少内存使用量。比如在一块连续的内存区域，15出现，则将第15位置1。 这个就是Bit Map算法。关于这个算法，网上有篇文章写得挺通俗易懂的，推荐：
优点：
1.运算效率高，不许进行比较和移位；
2.占用内存少，比如N=10000000；只需占用内存为N/8=1250000Byte=1.25M。
缺点：
       所有的数据不能重复。即不可对重复的数据进行排序和查找。
3、 Map映射表
假设需要排序或者查找的总数N=10000000，那么我们需要申请内存空间的大小为int a[1 + N/32]，其中：a[0]在内存中占32为可以对应十进制数0-31，依次类推：
bitmap表为：
a[0]--------->0-31
a[1]--------->32-63
a[2]--------->64-95
a[3]--------->96-127
..........
那么十进制数如何转换为对应的bit位，下面介绍用位移将十进制数转换为对应的bit位。
4、 Bit-Map的应用
      1）可进行数据的快速查找，判重，删除，一般来说数据范围是int的10倍以下。
       2）去重数据而达到压缩数据
如果用Bit Map算法，一个整数用一位表示出现与否，需要的内存大小是：
4 * 10^9 b = 0.5 * 10^9 B = 0.5GB
而我们有1GB的内存，因此该算法可行。由于Bit Map只能处理非负数， (没有说在第-1位上置1的)，因此对于有符号整数，可以将所有的数加上0x7FFFFFFF， 将数据移动到正半轴，找到一个满足条件的数再减去0x7FFFFFFF即可。 因此本文只考虑无符号整数，对于有负数的情况，按照上面的方法处理即可。
我们遍历一遍文件，将出现的数对应的那一位置1，然后遍历这些位， 找到第一个有0的位即可，这一位对应的数没有出现。代码如下：
第二问，如果我们只有10MB的内存，明显使用Bit Map也无济于事了。 内存这么小，注定只能分块处理。

12.4
You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4KB of memory available, how would you print all duplicate elements in the array?
我们有4KB的内存，一共有4 * 210 * 8位，大于32000，所以我们可以用Bit Map 来做这道题目。题目很简单，不过我们可以把代码写得漂亮一些。 我们可以写一个Bit Map类来完成基本的位操作。

12.5
If you were designing a web crawler, how would you avoid getting into infinite loops?
看完这题，建议用python写个爬虫，对此就能理解的多一些，而且还可以做出好玩的东西。
话说爬虫为什么会陷入循环呢？答案很简单，当我们重新去解析一个已经解析过的网页时， 就会陷入无限循环。这意味着我们会重新访问那个网页的所有链接， 然后不久后又会访问到这个网页。最简单的例子就是，网页A包含了网页B的链接， 而网页B又包含了网页A的链接，那它们之间就会形成一个闭环。
那么我们怎样防止访问已经访问过的页面呢，答案也很简单，设置一个标志即可。 整个互联网就是一个图结构，我们通常使用DFS(深度优先搜索)和BFS(广度优先搜索) 进行遍历。所以，像遍历一个简单的图一样，将访问过的结点标记一下即可。
(或者加上timestamp，虽然可能有搜不到的，但是快捷，trade off)

12.6
You have a billion urls, where each is a huge page. How do you detect the duplicate documents?
解答
To prevent infinite loops, we just need to detect cycles.One way to do this is to create a hash table where we set hash[v] to true after we visit page v.
网页大，数量多，要把它们载入内存是不现实的。 因此我们需要一个更简短的方式来表示这些网页。而hash表正是干这事的。 我们将网页内容做哈希，而不是url，这里不同url可能对应相同的网页内容。
将每个网页转换为一个哈希值后，我们就得到了10亿个哈希值， 很明显，两两对比也是非常耗时的O(n2 )。因此我们需要使用其它高效的方法。
根据以上分析，我们可以推出满足条件的以下算法：
遍历网页，并计算每个网页的哈希值。
检查哈希值是否已经在哈希表中，如果是，说明其网页内容是重复的，输出其url。 否则保存url，并将哈希值插入哈希表。
通过这种方法我们可以得到一组url，其对应的网页内容都是唯一的。但有一个问题， 一台计算机可以完成以上任务吗？
一个网页我们要花费多少存储空间？
每个网页转换成一个4字节的哈希值
假设一个url平均是30个字符，那我们至少需要30个字节
因此对应一个url，我们一共要用掉34个字节
34字节 * 10亿 = 31.6GB。很明显，单机的内存是无法搞定的。
我们要如何解决这个问题？
我们可以将这些数据分成多个文件放在磁盘中，分次载入内存处理。 这样一来我们要解决的就是文件的载入/载出问题。
我们可以通过哈希的方式将数据保存在不同文件，这样一来，大小就不是问题了， 但存取时间就成了问题。硬盘上的哈希表随机读写要耗费较多的时间， 主要花费在寻道及旋转延迟上。关于这个问题， 可以使用电梯调度算法来消除磁头在磁道间的随机移动，以此减少消耗的时间。
我们可以使用多台机器来处理这些数据。这样一来，我们要面对的就是网络延迟。 假如我们有n台机器。
首先，我们对网页做哈希，得到一个哈希值v
v%n 决定这个网页的哈希值会存放在哪台机器
v/n 决定这个哈希值存放在该机器上哈希表的位置

12.7
You have to design a database that can store terabytes of data. It should support efficient range queries. How would you do it?
首先要明确，并不是所有的字段都可以做区间查询。比如对于一个员工， 性别就没有所谓的区间查询；而工资是可以做区间查询的， 例如查询工资大于a元而小于b元的员工。
我们将需要做区间查询的字段对应的字段值提取出来作为关键字构建一棵B+树， 同时保存其对应记录的索引。B+树会对关键字排序，这样我们就可以进行高效的插入， 搜索和删除等操作。我们给定一个查询区间，在B+ 树中找到对应区间开始的结点只需要O(h)的时间，其中h是树高，一般来说都很小。 叶子结点保存着记录的索引，而且是按关键字(字段值)排好序的。 当我们找到了对应区间开始的叶子结点，再依次从其下一个块中找出对应数量的记录， 直到到到查询区间右端(即最大值)为止。这一步的时间复杂度由其区间中元素数量决定。
避免使用将数据保存在内部结点的树(B+树将数据都保存在叶子结点)， 这样会导致遍历树的开销过大(因为树并非常驻内存)。
假设这棵B+树上对应的数字表示工资，单位千元。员工对应的工资数据， 其实就都保存在叶子结点上，内部结点和根结点保存的只是其子结点数据的最大值。 这里假设每个叶子结点上的工资值所在的那条记录索引并没有画出来。OK， 现在我们要查询工资大于25k小于60k的员工记录。
B+树常用于数据库和操作系统的文件系统中，你值得了解XD。



"""