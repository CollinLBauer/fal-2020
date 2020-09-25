## Assignment 3 - Tuple Calculus

Collin Bauer

---

## 1. 5.12 problems

### b) List all single rooms with a price below £20 per night.
- { R | Room(R) ^ R.price < 20 }

### c) List the names and cities of all guests.
- { G.guestName, H.city | Hotel(H) ^ (∃R)(∃G)(Room(R) ^ Guest(G) ^ H.hotelNo = R.hotelNo ^ G.guestNo = R.guestNo) }

### e) List all guests currently staying at the Grosvenor Hotel.
- { G.guestName | Guest(G) ^ (∃H)(∃B)(Hotel(H) ^ Booking(B) ^ B.guestNo = G.guestNo ^ H.hotelNo = B.hotelNo ^ B.dateFrom < "15-SEP-2020" ^ B.dateTo > "15-SEP-2020" ^ H.hotelName = "Grosvenor") }

### g) List the guest details (guestNo, guestName, and guestAddress) of all guests staying at the Grosvenor Hotel.
- { G.guestNo, G.guestName, G.guestAddress | Guest(G) ^ (∃H)(∃B)(Hotel(H) ^ Booking(B) ^ B.guestNo = G.guestNo ^ H.hotelNo = B.hotelNo ^ H.hotelName = "Grosvenor") }

<br/>

## 2. More queries

### a) Get a listing of the names of hotels that have a hotel in Cambridge.
- { H.hotelName | Hotel(H) ^ H.city = "Cambridge" }

### b) Get a listing of the names of hotels that do *not* have a hotel in Cambridge.
- { H.hotelName | Hotel(H) ^ H.city ≠ "Cambridge" }

### c) Get a listing of the guest numbers of guests who have had a booking with every hotel in Stratford.
- { B.guestNo | Booking(B) ^ (∃H)(Hotel(H) ^ B.hotelNo = H.hotelNo ^ H.hotelName = "Stratford") }

<br/>

## 3. 5.10 problems

### a) Lists all hotel names where the hotel is in the city London
### b) Lists all hotel names that have a room with a price greater than £50
### c) Lists all hotel names which have had a guest named "John Smith"

<br/>

## 4. 5.9 problems (tuple equivalents)

### a) { R.hotelNo | Room(R) ^ R.price > 50)}
### b) { T | (∃R)(∃H)(Hotel(H) ^ Room(R) ^ T.hotelNo = T.hotelNo ^ T.hotelName = H.hotelname ^ T.city = H.city ^ T.roomNo = R.roomNo ^ T.type = R.type ^ T.price = H.price ^ H.hotelNo = R.hotelNo)}
### c) { H.hotelName | Hotel(H) ^ (∃R)(Room(R) ^ H.hotelNo = R.hotelNo ^ R.price > 50) }
### f) { T.hotelName, T.hotelNo | T ^ (∃B)(∃G)(∃H)(Booking(B) ^ Guest(G) ^ Hotel(H) ^ T.hotelNo = B.hotelNo ^ T.guestNo = B.guestNo ^ T.dateFrom = B.dateFrom ^ T.dateTo = B.dateTo ^ T.roomNo = B.roomNo ^ B.guestNo = G.guestNo ^ T.hotelName = H.hotelName ^ ( T.hotelNo = H.hotelNo -> H.city != "london")) }