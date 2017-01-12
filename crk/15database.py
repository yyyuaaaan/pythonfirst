"""__author__ = 'anyu'"""
"""
Note that each apartment can have multiple tenants, and each tenant can have multiple apartments. Each apartment belongs to one building, and each building belongs to one complex.
15.1 Write a method to find the number of employees in each department.
The LEFT JOIN keyword returns all rows from the left table (table1), with the matching rows in the right table (table2). The result is NULL in the right side when there is no match.
这个问题可以先将部门表和员工表做连接，然后再统计每个部门中的员工数量。 这里使用左连接，因为对于0个员工的部门，我们也要包含进来。
select Dept_Name, Departments.Dept_ID, count(*) as 'num_employees'
from Departments
left join Employees
on Employees.Dept_ID = Departments.Dept_ID
group by Departments.Dept_ID, Dept_Name

15.2 What are the different types of joins? Please explain how they differ and why certain types are better in certain situations.
连接(JOIN)将数据库中的两个或多个表组合起来。为了使用连接， 每个表至少要包含一个相同的字段(属性)。不同的连接类型决定了哪些记录会出现在结果集。
1. 内连接(INNER JOIN)：结果只包含两个表中严格匹配的记录。 本例中只返回3条记录，1条COCACOLA的和2条PEPSI的。SQL语句如下：
SELECT * from RB INNER JOIN CFB ON RB.Code = CFB.Code
2. 外连接(OUTER JOIN)：外连接一定包含内连接的结果，但同时还包含一些别的记录。 外连接可分为以下类型：
2.1 左外连接(LEFT OUTER JOIN)：简称左连接(LEFT JOIN)， 结果包含左边的表中所有记录，对于与右表没有匹配的记录，来自右表的所有列设为NULL， 本例中会返回4条记录，除了内连接的3个结果，BUDWEISER也会被列出来。SQL语句如下：
SELECT * from RB LEFT OUTER JOIN CFB ON RB.Code = CFB.Code
2.2 右外连接(RIGHT OUTER JOIN)简称右连接(RIGHT JOIN)， 右连接与左连接相反，结果将包含右表中的所有记录。右连接很少使用， 因为它总是可以被替换成左连接，只需要交换两表的位置即可。
2.3 全连接(FULL OUTER JOIN)全连接是左右连接的并集， 结果集中包含被连接表的所有记录，如果缺少匹配的记录，即以NULL填充。本例子中， 全连接会得到6条记录。SQL语句如下：
SELECT * from RB FULL OUTER JOIN CFB ON RB.Code = CFB.Code
JOIN is used to combine the results of two tables.T o perform a DOIN, each of the tables must have at least one field that will be used to find matching records from the other table. The join type defines which records will go into the result set.

15.3 What is denormalization? Explain the pros and cons. 用cache来做比喻
Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database.
反范式是通过增加冗余数据或数据分组来提高数据库读性能的过程。在某些情况下， 反范式有助于掩盖关系型数据库软件的低效。关系型的范式数据库即使做过优化， 也常常会带来沉重的访问负载。

数据库的范式设计会存储不同但相关的信息在不同的逻辑表， 如果这些表的存储在物理上也是分离的，那么从几个表中完成数据库的查询可能就会很慢 (比如JOIN操作)。如果JOIN操作的表很多，那么可能会慢得离谱。 有两个办法可以解决这个问题。首选的方法是使逻辑上的设计遵循范式， 但允许数据库管理系统(DBMS)在磁盘上存储额外的冗余信息来加快查询响应。 在这种情况下，DBMS还要保证冗余副本与原始数据的一致性。 这种方法通常在SQL中以索引视图(微软的SQL Server)或物化视图(Oracle)实现。 视图将信息表示为方便查询的格式，索引确保视图上的查询进行了优化。

更常见的做法是对数据做反范式设计。这种方法同样能提高查询响应速度， 但此时不再是DBMS而是数据库设计者去保证数据的一致性。 数据库设计者们通过在数据库中创建规则来保证数据的一致性，这些规则叫约束。 这样一来，数据库设计的逻辑复杂度就增加了，同时额外约束的复杂度也增加了， 这使该方法变得危险。此外，“约束”在加快读操作(SELECT)的同时，减慢了写操作 (INSERT, UPDATE和DELETE)。这意味着一个反范式设计的数据库， 可能比它的范式版本有着更差的写性能。

反范式数据模型与没有范式化的数据模型不同。 只有在范式化已经达到一定的满意水平并且所需的约束和规则都已经建立起来， 才进行反范式化。例如，所有的关系都属于第三范式， 连接的关系和多值依赖得到了妥善处理。

15.4 Draw an entity-relationship diagram for a database with companies, people, and professionals (people who work for companies).
在公司中工作的人(people)是专业人士(professionals)，因此， professionals和people间是ISA(is a)的关系。 或者，我们可以说professionals是从people派生出来的。

除了people的属性，每个professional还有自己额外的属性，如：级别，工作经验等。

一个professional只能去一家公司上班(一般情况下是这样)， 而一家公司可以雇佣很多的professional。因此，它们之间是多对一的关系。 “工作(work for)"关系可以有如下属性：加入公司的时间，工资等。 为什么这两个属性是关系的属性而不是professional的属性呢？ 因为只有当我们将professional和companies联系起来，才会有这些属性， 或是说这些属性才有意义。

一个人可以有多个电话号码，因此电话号码是一个多值属性。

15.5 Imagine a simple database storing information for students’ grades. Design what this database might look like, and provide a SQL query to return a list of the honor roll students (top 10%), sorted by their grade point average.
在一个简单的数据库中，我们至少需要以下三张表：学生表(Students)，课程表(Courses)， 及课程登记表(CourseEnrollment)。学生表中至少需要有学生姓名和学生ID， 及其它的个人信息。课程表包含课程名和课程ID，还可以包含课程描述和授课老师等。 课程登记表将包含学生和课程对(即哪个学生选了什么课，某课程有哪些学生选)， 还包含课程成绩等。我们假设课程成绩是一个整数。
SELECT StudentName, GPA
FROM (
    SELECT   top 10 percent Avg(CourseEnrollment.Grade) AS GPA,
    CourseEnrollment.StudentID
    FROM CourseEnrollment
    GROUP BY CourseEnrollment.StudentID
    ORDER BY Avg(CourseEnrollment.Grade)) Honors
INNER JOIN Students
ON Honors.StudentID = Students.StudentID
Be very careful about what implicit assumptions you make.
However, you WILL need to make some assumptions, or you'd drive yourself crazy. Which assumptions you make is less important than just recognizing that you made assumptions. Incorrect assumptions, both in the real world and in an interview, can be dealt with as long as they are acknowledged.
Remember, additionally, that there's a trade-off between flexibility and complexity.

"""

"""
15.1 Write a SQL query to get a list of tenants who are renting more than one apartment.
SELECT TenantName
FROM Tenants
INNER DOIN
   (SELECT TenantID
   FROM AptTenants
   GROUP BY TenantID
   HAVING count(*) > 1) C
ON Tenants.TenantID=C.TenantID
Whenever you write a GROUP BY clause in an interview (or in real life), make sure that anything in the SELECT clause is either an aggregate function or contained within the GROUP BY clause.

15.2 Write a SQL query to get a list of all buildings and the number of open requests
 (Requests in which status equals 'Open').
This problem uses a straightforward join of Requests and Apartments to get a list of building IDs and the number of open requests. Once we have this list, we join it again with the Buildings table.
SELECT BuildingName, ISNULL(Count, 0) as 'Count'
FROM Buildings
LEFT DOIN
  (SELECT Apartments.BuildingID, count(*) as 'Count'
  FROM Requests INNER DOIN Apartments
  ON Requests.AptID = Apartments.AptID
  WHERE Requests.Status = 'Open'
  GROUP BY Apartments.BuildingID) ReqCounts
ON ReqCounts.BuildingID = Buildings.BuildingID
Queries like this that utilize sub-queries should be thoroughly tested, even when coding by hand. It may be useful to test the inner part of the query first, and then test the outer part.

15.3 Building #11 is undergoing a major renovation. Implement a query to close all requests from apartments in this building.
UPDATE Requests
SET Status='Closed'
WHERE AptID IN
 (SELECT AptID
 FROM Apartments
 WHERE BuildingID = 11)


"""