create database eventapplication;

use eventapplication;

Create table Users (
user_id Int Auto_Increment Primary key ,
full_name varchar(100) not null,
email varchar(100) unique not null,
city varchar(100) not null,
registration_date date not null);

Create table Events (
event_id int primary key auto_increment,
title varchar(200) not null,
description text ,
city varchar(100) not null,
start_date datetime not null,
end_date datetime not null,
status enum ('upcoming','completed','cancelled'),
organizer_id int ,
foreign key(organizer_id) references Users(user_id)
);

Create table Sessions(
session_id int primary key auto_increment,
event_id int,
foreign key(event_id) references Events(event_id),
title varchar(100) not null,
speaker_name varchar(100) not null,
start_time datetime not null,
end_time datetime not null);

Create table Registrations(
registration_id int primary key auto_increment,
user_id int ,
event_id int,
registration_date date not null,
foreign key(user_id) references Users(user_id),
foreign key(event_id) references Events(event_id));

Create table Feedback(
feedback_id int primary key auto_increment,
user_id int,
event_id int,
rating int Check(rating between 1 and 5),
comments text,
feedback_date date not null,
foreign key(user_id) references Users(user_id),
foreign key(event_id) references Events(event_id)
);

Create table Resources(
resource_id int primary key auto_increment,
event_id int,
resource_type enum('pdf','image','link'),
resource_url varchar(255) not null,
uploaded_at datetime not null,
foreign key(event_id) references Events(event_id)
);

UPDATE Sessions
SET event_id = 1
WHERE session_id = 1;

UPDATE Sessions
SET event_id = 1
WHERE session_id = 2;

UPDATE Sessions
SET event_id = 2
WHERE session_id = 3;

UPDATE Sessions
SET event_id = 3
WHERE session_id = 4;

UPDATE Events
SET organizer_id = 1
WHERE event_id = 1;

UPDATE Events
SET organizer_id = 3
WHERE event_id = 2;

UPDATE Events
SET organizer_id = 2
WHERE event_id = 3;