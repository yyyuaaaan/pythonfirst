""""""
"""


8.1 Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack(twenty-one).
 Get 21 points on your first two cards (called a blackjack), without a dealer blackjack;
Reach a final score higher than the dealer without exceeding 21; or
Let the dealer draw additional cards until his hand exceeds 21.

 It is important to ask your interviewer what she means by generic.
Let's assume that your interviewer clarifies that the deck is a standard 52-card set,

8.2 Imagine you have a call center with three levels of employees: respondent, manager, and director. An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not free or notable to handle it, then the call should be escalated to a director. Design the classes and data structures for this problem. Implement a method dispatchCaL L() which assigns a call to the first available employee.

 We should keep-these things within their respective class.
 a few things which are common to them, like address, name, job title, and age. These things can be kept in one class

Note that on any object-oriented design question, there are many ways to design the objects. Discuss the trade-offs of different solutions with your interviewer.You should usually design for long-term code flexibility and maintenance.

CallHandler is implemented as a singleton class.

Call represents acall froma user. A call hasa minimumrank and isassigned to the first employee who can handle it.

Employee is a super class for the Director, Manager, and Respondent classes. It is implemented as an abstract class since there should be no reason to instantiate an Employee type directly.

The Respondent, Director, and Manager classes are now just simple extensions of the Employee class.

This may seem like an awful lot of code to write in an interview, and it is.We've been much more thorough here than you would need. In a real interview, you would likely be much lighter on some of the details until you have time to fill them in.

8.3 Design a musical juke box using object-oriented principles.
8.4 Design a parking lot using object-oriented principles.
The wording of this question is vague, just as it would be in an actual interview. This requires you to have a conversation with your interviewer about what types of vehicles it can support, whether the parking lot has multiple levels, and so on.
8.5 Design the data structures for an online book reader system.

• User membership creation and extension.
• Searching the database of books.
• Reading a book.
• Only one active user at a time
• Only one active book by this user.

8.6 Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle. Youcan assume that you have a fitsWith method which, when passed two puzzle pieces, returns true if the two pieces belong together.

8.7 Explain how you would design a chat server. In particular, provide details about the various backend components, classes, and methods. What would be the hardest problems to solve?
We will assume that "friending" is mutual; I am only your contact if you are mine. Our chat system will support both group chat and one-on-one (private) chats. We will not worry about voice chat, video chat, or file transfer.
What problems would be the hardest to solve (or the most interesting)?
Q7: How do we know if someone is online—/ mean, really, really know?
Q2:Howdowedealwithconflicting information?
Q3: How do we make our server scale?
Q4: How we do prevent denial of service attacks?

8.9 Explain the data structures and algorithms that you would use to design an in-memory file system. Illustrate with an example in code where possible.
8.10 Design and implement a hash table which uses chaining (linked lists) to handle collisions.
Suppose we are implementing a hash table that looks like HasrKK, V>. That is, the hash table maps from objects of type K to objects of type V.
hash both <K,V> pairs in to a index or array of linkedlist
In computing, a hash table (also hash map) is a data structure used to implement an associative array, a structure that can map keys to values.
"""