#create table
CREATE TABLE Person(
    id int primary key,
    name varchar(255),
    address varachar(255),
    age int,
    mobile int
)


CREATE TABLE Fruits(
    id int primary key,
    name varchar(255),
    colour varchar(255),
    size varchar(255),
    price int
)

CREATE TABLE Players(
    id int primary key,
    name varchar(255),
    team varchar(255),
    jersey int,
    runs int,
)

CREATE TABLE State(
    id int primary key,
    name varchar(255),
    capital city varchar(255),
    language varchar(255),
    population int,
)


# Insert Data

INSERT INTO Person(name,address,age,mobile)
VALUES('Hrithwik','Gokulam',28,8281278872)

INSERT INTO Fruits(name,colour,size,price)
VALUES('Apple','Red','Small',200)
