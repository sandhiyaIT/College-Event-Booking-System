create table Users(
student_id number primary key,
name varchar2(100),
email varchar2(100), 
password varchar2(100)
);

create table Events(
event_id number primary key,
event_name varchar2(100),
event_date date,
venue varchar2(100),
total_seats number,
ticket_price number
);

create table Bookings(
booking_id number GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
student_id number,
event_id number,
tickets number
);
