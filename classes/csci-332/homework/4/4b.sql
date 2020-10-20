-- Collin Bauer
-- Assignment 4, part B

-- #1
select city as propertyCity, fName as ownerFName,
lName as ownerLName, address as ownerAddr
from dreamhome.propertyforrent
inner join dreamhome.privateowner
on propertyforrent.ownerNo = privateowner.ownerNo;

-- #2
select clientNo from dreamhome.viewing
inner join dreamhome.propertyforrent
on propertyforrent.propertyNo = viewing.propertyNo
where city = "Aberdeen";

-- #3
select fName, lName, eMail
from dreamhome.client as c
inner join dreamhome.viewing as v on c.clientNo = v.clientNo
inner join dreamhome.propertyforrent as p on p.propertyNo = v.propertyNo
where city = "Aberdeen" or city = "London";

-- #4
select c.fName, c.lName, c.eMail
from dreamhome.propertyforrent as p
inner join dreamhome.viewing as v on v.propertyNo = p.propertyNo
inner join dreamhome.branch as b on b.branchNo = p.branchNo
inner join dreamhome.client as c on c.clientNo = v.clientNo
where b.city = "Glasw";

-- #5
select p.street, p.city, p.postcode, p.type
from dreamhome.propertyforrent as p
left join dreamhome.viewing as v on p.propertyNo = v.propertyNo
where v.clientNo is null;

-- #6 
select c.fName, c.lName, p.street, p.city, p.postcode
from dreamhome.client as c
inner join dreamhome.viewing as v on c.clientNo = v.clientNo
inner join dreamhome.propertyforrent as p on p.propertyNo = v.propertyNo;

-- #7
-- Staffless viewings, yikes.
select p.staffNo
from dreamhome.propertyforrent as p
inner join dreamhome.viewing as v on v.propertyNo = p.propertyNo
group by v.propertyNo
having count(v.propertyNo) > 1;

-- #8
-- Well I guess I already answered this in 4a, oops
select *
from dreamhome.staff
where s.position = "Manager" and exists(
    select *
    from dreamhome.staff
    group by branchNo having count(branchNo) >= 2
);