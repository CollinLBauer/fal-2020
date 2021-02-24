-- create database universityclb
use universityclb;

create table DEPARTMENT (
	DID CHAR(4),
	DeptName VARCHAR(30) NOT NULL,
	OfficeLocation VARCHAR(255),
	ChairID CHAR(8),
	PRIMARY KEY (DID)
);