# Pothering's Chapter 2 - Relational Algebra and Tuple Calculus
### Book chapters covered:
- ?

### Lectures included:
- 09/17
- 09/29

---

# SQL - Strutured Qurey Language

## SQL commands
- **SELECT** - Projection, the elements desired *(NOT a selection)*
- **FROM** - Referenced table, OR Cartesian Product if more than one table
- **WHERE** - Selection, a conditional
- **ORDER-BY** - how to sort the list
  - *ASC* (default) sorts by ascending order
  - *DESC* sorts by descending order
  - accepts a list of attributes to cascading sort by
- **EXISTS**

### Logical operators
- =
- NOT
- AND
- OR

### Special variables
- * - wildcard, "everything"

### Notes on SQL
- SQL is *not* case sensitive. However, it is usually written in capitalized forms for readbility.

## SELECT

## EXISTS

## EXCEPT
- Essentially division


## SQL Examples

What are the student numbers of all students not yet enrolled in a class?
- Relational Algebra:  
  Π<sub>STID</sub>(STUDENT) - Π<sub>STID</sub>(ENROLLMENT)
- Tuple calculus:  
  {s[STID]|s}
- SQL:
  (SELECT SID FROM STUDENT) EXCEPT (SELECT STID FROM ENROLLMENT)