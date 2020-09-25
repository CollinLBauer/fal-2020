## Assignment 2 - Relational Algebra

Collin Bauer

---

## 1. 5.12 problems

### b) List all single rooms with a price below £20 per night.
- σ<sub>price < 20 ^ type = "single"</sub>(Rooms)

### c) List the names and cities of all guests.
- Π<sub>guestName,city</sub>(Booking ⋈ Hotel ⋈ Guest)

### e) List all guests currently staying at the Grosvenor Hotel.
- Π<sub>guestName</sub>(σ<sub>hotelName = "Grosvenor" ^ dateFrom < "15-SEP-2020" ^ dateTo > "15-SEP-2020"</sub>(Booking ⋈ Hotel ⋈ Guest))

### g) List the guest details (guestNo, guestName, and guestAddress) of all guests staying at the Grosvenor Hotel.
- Π<sub>guestNo, guestName, guestAddress</sub>(σ<sub>hotelName = "Grosvenor"</sub>(Booking ⋈ Hotel ⋈ Guest))

<br/>

## 2. More queries

### a) Get a listing of the names of hotels that have a hotel in Cambridge.
- Π<sub>hotelName</sub>(σ<sub>city = "Cambridge"</sub>(Hotel))

### b) Get a listing of the names of hotels that do *not* have a hotel in Cambridge.
- Π<sub>hotelName</sub>(σ<sub>city != "Cambridge"</sub>(Hotel))

### c) Get a listing of the guest numbers of guests who have had a booking with every hotel in Stratford.
- Π<sub>guestNo</sub>(σ<sub>city = "Stratford"</sub>(Booking ⋈ Hotel))

<br/>

## 3. 5.8 problems

### a) Lists all hotel numbers whose room price is greater than £50
### b) Creates a new table with all hotel rooms and their corresponding hotel data
### c) Lists all hotel names that has a room with a price greater than £50
### f) Lists all guest names and hotel numbers of guests who stayed at a hotel in London