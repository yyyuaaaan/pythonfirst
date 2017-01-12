"""__author__ = 'anyu'
"""
"""
13.1 Write a method to print the last K lines of an input file using C++.

13.2 Compare and contrast a hash table vs. an STL map. How is a hash table implemented?If the number of inputs is small, what data structure options can be used instead of a hash table?
对比哈希表和STL map
在哈希表中，实值的存储位置由其键值对应的哈希函数值决定。因此， 存储在哈希表中的值是无序的。在哈希表中插入元素和查找元素的时间复杂度都是O(1)。 (假设冲突很少)。实现一个哈希表，冲突处理是必须要考虑的。
对于STL中的map，键/值对在其中是根据键进行排序的。它使用一根红黑树来保存数据， 因此插入和查找元素的时间复杂度都是O(logn)。而且不需要处理冲突问题。 STL中的map适合以下情况使用：
查找最小元素
查找最大元素
有序地输出元素
查找某个元素，或是当元素找不到时，查找比它大的最小元素

哈希表是怎么实现的
首先需要一个好的哈希函数来确保哈希值是均匀分布的。比如：对大质数取模
其次需要一个好的冲突解决方法：链表法(chaining，表中元素比较密集时用此法)， 探测法(probing，开放地址法，表中元素比较稀疏时用此法).
动态地增加或减少哈希表的大小。比如，(表中元素数量)/(表大小)大于一个阈值时， 就增加哈希表的大小。我们新建一个大的哈希表，然后将旧表中的元素值， 通过新的哈希函数映射到新表。
如果输入数据规模不大，我们可以使用什么数据结构来代替哈希表。
你可以使用STL map来代替哈希表，尽管插入和查找元素的时间复杂度是O(logn)， 但由于输入数据的规模不大，因此这点时间差别可以忽略不计。

13.3 How do virtual functions work in C++?
虚函数依赖虚函数表进行工作。如果一个类中，有函数被关键词virtual进行修饰， 那么一个虚函数表就会被构建起来保存这个类中虚函数的地址。同时， 编译器会为这个类添加一个隐藏指针指向虚函数表。如果在派生类中没有重写虚函数， 那么，派生类中虚表存储的是父类虚函数的地址。每当虚函数被调用时， 虚表会决定具体去调用哪个函数。因此，C++中的动态绑定是通过虚函数表机制进行的。
当我们用基类指针指向派生类时，虚表指针vptr指向派生类的虚函数表。 这个机制可以保证派生类中的虚函数被调用到。


13.4 What is the difference between deep copy and shallow copy? Explain how you would use each.
浅拷贝并不复制数据，只复制指向数据的指针，因此是多个指针指向同一份数据。 深拷贝会复制原始数据，每个指针指向一份独立的数据。通过下面的代码， 可以清楚地看出它们的区别：
浅拷贝在构造和删除对象时容易产生问题，因此使用时要十分小心。如无必要， 尽量不用浅拷贝。当我们要传递复杂结构的信息，而又不想产生另一份数据时， 可以使用浅拷贝，比如引用传参。浅拷贝特别需要注意的就是析构时的问题， 当多个指针指向同一份内存时，删除这些指针将导致多次释放同一内存而出错。
实际情况下是很少使用浅拷贝的，而智能指针是浅拷贝概念的增强。 比如智能指针可以维护一个引用计数来表明指向某块内存的指针数量， 只有当引用计数减至0时，才真正释放内存。
大部分时候，我们用的是深拷贝，特别是当拷贝的结构不大的时候。

13.5 What is the significance of the keyword “volatile” in C?
volatile的意思是"易变的"，因为访问寄存器比访问内存要快得多， 所以编译器一般都会做减少存取内存的优化。volatile 这个关键字会提醒编译器，它声明的变量随时可能发生变化(在外部被修改)， 因此，与该变量相关的代码不要进行编译优化，以免出错。

13.6 What is name hiding in C++?
让我们通过一个例子来讲解C++中的名字隐藏。在C++中，如果一个类里有一个重载的方法， 你用另一个类去继承它并重写(覆盖)那个方法。你必须重写所有的重载方法， 否则未被重写的方法会因为名字相同而被隐藏，从而使它在派生类中不可见。
名字隐藏与虚函数无关。所以不管基类中那两个函数是不是虚函数， 在这里都会发生名字隐藏。解决方法有两个。第一个是将2个参数的MethodA换一个名字， 那么它在派生类中就可见了。但我们既然重载了MethodA，说明它们只是参数不同， 而实际上应该是在做相同或是相似的事的。所以换掉名字并不是个好办法。因此， 我们一般采用第二种方法，在派生类中重写所有的重载函数。

13.7 Why does a destructor in base class need to be declared virtual?

13.8 Write a method that takes a pointer to a Node structure as a parameter and returns a complete copy of the passed-in data structure. The Node structure contains two pointers to other Node structures.
写一个函数，其中一个参数是指向Node结构的指针，返回传入数据结构的一份完全拷贝。 Node结构包含两个指针，指向另外两个Node。

13.9 Write a smart pointer (smart_ptr) class.
比起一般指针，智能指针会自动地管理内存(释放不需要的内存)，而不需要程序员去操心。 它能避免迷途指针(dangling pointers)，内存泄漏(memory leaks)， 分配失败等情况的发生。智能指针需要为所有实例维护一个引用计数， 这样才能在恰当的时刻(引用计数为0时)将内存释放。



"""
