"""__author__ = 'anyu'"""
"""
18.1 What’s the difference between a thread and a process?
这是一道出现频率极高的面试题，考察基本概念。
进程可以认为是程序执行时的一个实例。进程是系统进行资源分配的独立实体， 且每个进程拥有独立的地址空间。一个进程无法直接访问另一个进程的变量和数据结构， 如果希望让一个进程访问另一个进程的资源，需要使用进程间通信，比如：管道，文件， 套接字等。
一个进程可以拥有多个线程，每个线程使用其所属进程的栈空间。 线程与进程的一个主要区别是，同一进程内的多个线程会共享部分状态， 多个线程可以读写同一块内存(一个进程无法直接访问另一进程的内存)。同时， 每个线程还拥有自己的寄存器和栈，其它线程可以读写这些栈内存。
线程是进程的一个特定执行路径。当一个线程修改了进程中的资源， 它的兄弟线程可以立即看到这种变化。
以下是分点小结：
进程是系统进行资源分配的基本单位，有独立的内存地址空间； 线程是CPU调度的基本单位，没有单独地址空间，有独立的栈，局部变量，寄存器， 程序计数器等。
创建进程的开销大，包括创建虚拟地址空间等需要大量系统资源； 创建线程开销小，基本上只有一个内核对象和一个堆栈。
一个进程无法直接访问另一个进程的资源；同一进程内的多个线程共享进程的资源。
进程切换开销大，线程切换开销小；进程间通信开销大，线程间通信开销小。
线程属于进程，不能独立执行。每个进程至少要有一个线程，成为主线程
A process can be thought of as an instance of a program in execution. A process is an independent entity to which system resources (e.g., CPUtime and memory) are allo- cated. Each process is executed in a separate address space, and one process cannot access the variables and data structures of another process. If a process wishes to access another process' resources, inter-process communications have to be used. These include pipes, files, sockets, and other forms.
A thread exists within a process and shares the process' resources (including its heap space). Multiple threads within the same process will share the same heap space. This is very different from processes, which cannot directly access the memory of another process. Each thread still has its own registers and its own stack, but other threads can read and write the heap memory.
A thread is a particular execution path of a process. When one thread modifies a process resource, the change is immediately visible to sibling threads.

18.2 How can you measure the time spent in a context switch?
这是一个棘手的问题，让我们先从可能的解答入手。
上下文切换(有时也称为进程切换或任务切换)是指CPU 的控制权从一个进程或线程切换到另一个。 （参考资料） 例如让一个正在执行的进程进入等待状态(或终止它)，同时去执行另一个正在等待的进程。 上下文切换一般发生在多任务系统中，操作系统必须把等待进程的状态信息载入内存， 同时保存正在运行的进程的状态信息(因为它马上就要变成等待状态了)。
为了解决这个问题，我们需要记录两个进程切换时第一条指令和最后一条指令的时间戳， 上下文切换就是这两个时间戳的差。
来看一个简单的例子，假设只有两个进程：P1和P2。
P1正在执行，而P2在等待。在某个时刻，操作系统从P1切换到P2。假设此时， P1执行到第N条指令，记录时间戳Time_Stamp(P1_N)，当本来在等待的P2 开始执行第1条指令，说明切换完成，记录时间戳Time_Stamp(P2_1)。因此， 上下文切换的时间为：Time_Stamp(P2_1) - Time_Stamp(P1_N
思路非常简单。问题在于，我们如何知道上下文切换是何时发生的？ 进程的切换是由操作系统的调度算法决定的。我们也无法记录进程中每个指令的时间戳。
另一个问题是：许多内核级线程也做上下文切换，而用户对于它们是没有任何控制权限的。
总而言之，我们可以认为，这最多只能是依赖于底层操作系统的近似计算。 一个近似的解法是记录一个进程结束时的时间戳，另一个进程开始的时间戳及排除等待时间。
如果所有进程总共用时为T，那么总的上下文切换时间为： T - (所有进程的等待时间和执行时间)
Another issue is that swapping is governed by the scheduling algorithm of the oper- ating system and there may be many kernel level threads which are also doing context switches. Other processes could be contending for the CPU or the kernel handling interrupts. The user does not have any control over these extraneous context switches. For instance, if at time tljn the kernel decides to handle an interrupt, then the context switch time would be overstated.

18.3 Implement a singleton design pattern as a template such that, for any given class Foo, you can call Singleton::instance() and get a pointer to an instance of a singleton of type Foo. Assume the existence of a class Lock which has acquire() and release() methods. How could you make your implementation thread safe and exception safe?
实现一个单例模式的模板，当给一个类Foo时，你可以通过Singleton::instance() 来得到一个指向Foo类单例的指针。假设我们现在已经有了Lock类，其中有acquire() 和release()两个方法，你要如何使你的实现线程安全且异常安全？
使一个程序线程安全的一般方法是，当线程获得对共享资源的写权限时，需要对共享资源加锁。 这样一来，当一个线程在修改资源时，另外的线程就不能修改它。

18.5 Suppose we have the following code:…
i) Can you design a mechanism to make sure that B is executed after A, and C is executed after B?
class Foo{
public:
    A(.....); /*If A is called, a new thread will be created and
               the corresponding function will be executed. */
    B(.....); /*same as above */
    C(.....); /*same as above */
};
Foo f;
f.A(.....);
f.B(.....);
f.C(.....);
ii) Suppose we have the following code to use class Foo.
Foo f;
f.A(.....); f.B(.....); f.C(.....);
f.A(.....); f.B(.....); f.C(.....);
We do not know how the threads will be scheduled in the OS. Can you design a mechanism to make sure that all the methods will be executed in sequence?

第一问，初始的两个信号量都为0，函数A执行完后，信号量s_a会加1，这时B才可执行。 B执行完后信号量s_b加1，这时C才可执行。以此保证A，B，C的执行顺序。 注意到函数A其实没有受到限制，所以A可以被多个线程多次执行。比如A执行3次， 此时s_a=3；然后执行B，s_a=2,s_b=1；然后执行C，s_a=2,s_b=0； 然后执行B，s_a=1,s_b=1。即可以出现类似这种序列：AAABCB。
Semaphore s_a(0);
Semaphore s_b(0);
A {
    /***/
    s_a.release(1); // 信号量s_a加1
}
B {
    s_a.acquire(1); // 信号量s_a减1
    /****/
    s_b.release(1); // 信号量s_b加1
}
C {
    s_b.acquire(1); // 信号量s_b减1
    /******/
}
第二问代码如下，与第一问不同，以下代码可以确保执行顺序一定严格按照： ABCABCABC…进行。因为每一时刻都只有一个信号量不为0， 且B中要获取的信号量在A中释放，C中要获取的信号量在B中释放， A中要获取的信号量在C中释放。这个保证了执行顺序一定是ABC。
Semaphore s_a(0);
Semaphore s_b(0);
Semaphore s_c(1);
A {
    s_c.acquire(1);
    /***/
    s_a.release(1);
}
B {
    s_a.acquire(1);
    /****/
    s_b.release(1);
}
C {
    s_b.acquire(1);
    /******/
    s_c.release(1);
}


16.6 You are given a class with synchronized method A and a normal method B. If you have two threads in one instance of a program, can they both execute A at thesame time? Can they execute A and B at the same time?
By applying the word synchronized to a method, we ensure that two threads cannot execute synchronized methods on the same object instance at the same time.
So, the answer to the first part really depends. If the two threads have the same instance of the object, then no, they cannot simultaneously execute method A. However, if they have different instances of the object, then they can.
Conceptually, you can see this by considering locks. A synchronized method applies a "lock" on all synchronized methods in that instance of the object. This blocks other threads from executing synchronized methods within that instance.
In the second part, it can.
Ultimately, the key concept to remember here is that only one synchronized method can be in execution per instance of that object.

"""

