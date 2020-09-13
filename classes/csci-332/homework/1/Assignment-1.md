## Assignment 1 - Hotel Database

Collin Bauer

---

<br/>

## 1. Tables

### Hotel
| hotelNo | hotelName | hotelCity |
|-|-|-|
| 1 | La Quinta | Charleston |
| 2 | La Quinta | Myrtle Beach |
| 3 | La Quinta | Columbia |

### Room
| roomNo | hotelNo | type | price |
|-|-|-|-|
| 117 | 1 | single | $250 |
| 213 | 2 | quad | $400 |
| 148 | 3 | single | $225 |
| 205 | 1 | double | $300 |
| 401 | 3 | penthouse | $1000 |
| 117 | 3 | double | $350 |
| 118 | 3 | double | $300 |

### Booking
| hotelNo | guestNo | dateFrom | dateTo | roomNo |
|-|-|-|-|-|
| 1 | 1551 | 09/05/2020 | 09/10/2020 | 117 |
| 1 | 1549 | 09/10/2020 | 09/12/2020 | 117 |
| 1 | 1552 | 09/05/2020 | 09/08/2020 | 205 |
| 1 | 1550 | 09/14/2020 | 09/19/2020 | 205 |
| 2 | 1551 | 09/12/2020 | 09/13/2020 | 213 |
| 2 | 1550 | 09/20/2020 | 09/25/2020 | 213 |
| 3 | 1553 | 09/20/2020 | 09/25/2020 | 401 |
| 3 | 1549 | 09/13/2020 | 09/15/2020 | 117 |
| 3 | 1550 | 09/01/2020 | 09/05/2020 | 118 |
| 3 | 1552 | 09/09/2020 | 09/12/2020 | 118 |

### Guest
| guestNo | guestName | guestAddress |
|-|-|-|
| 1549 | John Wick |  |
| 1550 | George Carlin | 5050 5th St, New York, NY |
| 1551 | John Doe | 1008 Imaginary Drive, Springfield, MA |
| 1552 | Jane Doe | 1008 Imaginary Drive, Springfield, MA |
| 1553 | Bruce Wayne | 1007 Mountain Drive, Gotham City |

<br/>

## 2. Schema

**Table**: Hotel
- **Attribute**: hotelNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: hotelName
  - **Type**: VARCHAR(12)
  - **Required**: yes
- **Attribute**: hotelCity
  - **Type**: VARCHAR(16)
  - **Required**: yes
- **Primary Key**: hotelNo

**Table**: Room
- **Attribute**: roomNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: hotelNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: type
  - **Type**: VARCHAR(12)
  - **Required**: no
- **Attribute**: price
  - **Type**: INTEGER
  - **Required**: no
- **Primary Key**: (roomNo, hotelNo)
- **Foreign Key**: hotelNo **References** Hotel(hotelNo)

**Table**: Booking
- **Attribute**: hotelNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: guestNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: dateFrom
  - **Type**: CHAR(10)
  - **Required**: yes
- **Attribute**: dateTo
  - **Type**: CHAR(10)
  - **Required**: yes
- **Attribute**: roomNo
  - **Type**: INTEGER
  - **Required**: yes
- **Primary Key**: (hotelNo, guestNo, dateFrom)
- **Foreign Key**: hotelNo **References** Hotel(hotelNo)
- **Foreign Key**: guestNo **References** Guest(guestNo)
- **Foreign Key**: roomNo **References** Room(roomNo)

**Table**: Guest
- **Attribute**: guestNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: guestName
  - **Type**: VARCHAR(24)
  - **Required**: yes
- **Attribute**: guestAddress
  - **Type**: VARCHAR(63)
  - **Required**: no
- **Primary Key**: guestNo

<br/>

## 3. Schemas, redesigned

**Table**: Room
- **Attribute**: roomID
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: roomNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: hotelNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: type
  - **Type**: VARCHAR(12)
  - **Required**: no
- **Attribute**: price
  - **Type**: INTEGER
  - **Required**: no
- **Primary Key**: roomID
- **Foreign Key**: hotelNo **References** Hotel(hotelNo)

**Table**: Booking
- **Attribute**: bookID
- **Type**: INTEGER
- **Required**: yes
- **Attribute**: hotelNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: guestNo
  - **Type**: INTEGER
  - **Required**: yes
- **Attribute**: dateFrom
  - **Type**: CHAR(10)
  - **Required**: yes
- **Attribute**: dateTo
  - **Type**: CHAR(10)
  - **Required**: yes
- **Attribute**: roomNo
  - **Type**: INTEGER
  - **Required**: yes
- **Primary Key**: bookID
- **Foreign Key**: hotelNo **References** Hotel(hotelNo)
- **Foreign Key**: guestNo **References** Guest(guestNo)
- **Foreign Key**: roomNo **References** Room(roomNo)