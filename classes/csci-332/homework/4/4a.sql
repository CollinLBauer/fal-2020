-- Collin Bauer
-- Assingment 4, part A

-- #1
select * from dreamhome.propertyforrent where city = "Glasgow";

-- #2
select fName, lName, address from dreamhome.privateowner
where address like "%Glasw%";

-- #3
select * from dreamhome.propertyforrent
where type = "Flat" and rent < 400 order by rent desc;

-- #4
select * from dreamhome.propertyforrent where city = "London";
-- Just the one.

-- #5
select avg(salary) from dreamhome.staff;
-- 17000

-- #6
-- This does not separate them out into different tables,
-- but it does show the relevant data.
select staffNo, branchNo from dreamhome.staff order by branchNo;

-- #7
select avg(salary), branchNo from dreamhome.staff group by branchNo;

-- #8
select staffNo from dreamhome.staff
where position = "Manager" and exists
(select * from dreamhome.staff group by branchNo having count(branchNo) >= 2);