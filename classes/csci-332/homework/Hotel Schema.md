Hotel Schema

The following tables form part of a database held in a relational DBMS:
> Hotel (hotelNo, hotelName, city)  
> Room (roomNo, hotelNo, type, price)  
> Booking (hotelNo, guestNo, dateFrom, dateTo, roomNo)  
> Guest (guestNo, guestName, guestAddress)  

where Hotel contains hotel details and hotelNo is the primary key;
- Room contains room details for each hotel and (roomNo, hoteINo) forms the primary key;
- Booking contains details of bookings and (hoteINo, guestNo, dateFrom) forms the primary key;
- Guest contains guest details and guestNo is the primary key