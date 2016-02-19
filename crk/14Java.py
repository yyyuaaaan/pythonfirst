"""__author__ = 'anyu'
"""
"""
本书用java实现的，所以本章节很少
14.1 In terms of inheritance, what is the effect of keeping a constructor private?
Declaring the constructor private will ensure that no one outside of the class can directly instantiate the class. In this case, the only way to create an instance of the class is to provide a static public method, as is done when using the Factory Method Pattern.

14.2 InJava,does the finally block get executed if we insert a return statement inside the try block of a try-catch-finally?
Yes, it will get executed. The finally block gets executed when the try block exits. Even when we attempt to exit within the try block (via a return statement, a continuestatement,abreakstatement oranyexception),thefinally blockwillstill be executed.
Note that there are some cases in which the fin a lly block will not get executed, such as the following:
• If the virtual machine exits during t r y / c a t c h block execution.
• Ifthe thread which isexecuting the try/catch block gets killed.

14.3 What is the difference between final,finally,and finalize?
Despite their similar sounding names, final, finally and finalize have very different purposes. To speak in very general terms, fin a l is used to control whether a variable,method, or class is"changeable." Thefinally keyword isused in atry/ catch block to ensure that a segment of code is always executed. The f inalizeQ method is called by the garbage collector once it determines that no more references exist.

14.4 Explain the difference between templates in C++ and generics in Java.
Many programmers consider the concepts of templates and generics to be equivalent simply because both allow you to do something along the lines of List<St ringx But, how each language does this, and why, varies significantly.
The implementation of Java generics is rooted in an idea of "type erasure." The use of Java generics didn't real'y change much about our capabilities; it just made things a bit prettier. Forthis reason, Java genericsare sometimes called"syntactic sugar."
This is quite different from C++. In C++, templates are essentially a glorified macro set, with the compiler creating a new copy of the template code for each type.
In Java, static variables would be shared across instances of MyClass, regardless of the different type parameters.
C++ templates can use primitive types, like in t. Java cannot and must instead use Integer.

14.5 Explain what object reflection is in Java and why it is useful.
Object Reflection is a feature in Java which provides a way to get reflective information about Java classes and objects, and perform operations such as:
1. Gettinginformationaboutthemethodsandfieldspresentinsidetheclassatruntime.
2. Creatinganewinstanceofaclass.
3. Gettingandsettingtheobjectfieldsdirectlybygettingfieldreference,regardlessof what the access modifier is.
Object reflection is useful for three main reasons:
1. It helps in observing or manipulating the runtime behavior of applications.
2. It can help in debugging or testing programs, as we have direct access to methods, constructors, and fields.
3. We can call methods by name when we don't know the method in advance.For example, we may let the user pass in a class name, parametersfor the constructor, and a method name. We can then use this information to create an object and call a method. Doing these operations without reflection would require a complex series of if-statements, if it's possible at all.

14.6 Implement a CircularArray class that supports an array-like data structure which can be efficiently rotated.The class should use a generic type, and should support iteration via thestandardfor (Obj o : CircularArray) notati
To implement the Iterator interface,we need to do the following:
• Modify the CircularArray<T> definition to add implements Iterable<T>.This willalsorequireustoaddaniterator() methodtoCircularArray<T>.
• Create a CircularArrayIterator<T> which implements Iterator<T>. This will also require usto implement, in the CircularArraylterator, the methods hasNextQ, next(),and remove().
When you get a problem like this one in an interview, there's a good chance you don't remember exactly what the various methods and interfaces are called. In this case, work through the problem as well as you can. If you can reason out what sorts of methods one might need, that alone will show a good degree of competency.


"""