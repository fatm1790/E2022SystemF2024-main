CREATE DATABASE SalesOrdersDelivery;


use SalesOrdersDelivery;


CREATE TABLE Categories (
	CategoryID int NOT NULL primary key ,
	CategoryDescription text NULL 
);


CREATE TABLE Customers (
	CustomerID int NOT NULL primary key,
	CustFirstName text NULL ,
	CustLastName text NULL ,
	CustStreetAddress text NULL ,
	CustCity text NULL ,
	CustState text NULL ,
	CustZipCode text NULL ,
	CustAreaCode smallint NULL ,
	CustPhoneNumber text NULL 
);


CREATE TABLE Employees (
	EmployeeID int NOT NULL primary key,
	EmpFirstName text NULL ,
	EmpLastName text NULL ,
	EmpStreetAddress text NULL ,
	EmpCity text  NULL ,
	EmpState text  NULL ,
	EmpZipCode text  NULL ,
	EmpAreaCode smallint NULL ,
	EmpPhoneNumber text NULL , 
	EmpBirthDate date NULL
);


CREATE TABLE Order_Details (
	OrderNumber int NOT NULL,
	ProductNumber int NOT NULL ,
	QuotedPrice decimal NULL ,
	QuantityOrdered smallint NULL,
    foreign key (OrderNumber) references Orders(OrderNumber),
    foreign key (ProductNumber) references Products(ProductNumber),
    primary key (OrderNumber, ProductNumber)
);


CREATE TABLE Orders (
	OrderNumber int NOT NULL primary key,
	OrderDate date NULL ,
	ShipDate date NULL ,
	CustomerID int NULL,
	EmployeeID int NULL ,
    foreign key (CustomerID) references Customers(CustomerID),
    foreign key (EmployeeID) references Employees(EmployeeID)
);


CREATE TABLE Product_Vendors (
	ProductNumber int NOT NULL,
	VendorID int NOT NULL ,
	WholesalePrice decimal NULL ,
	DaysToDeliver int NULL,
    foreign key (ProductNumber) references Products (ProductNumber),
    foreign key (VendorID) references Vendors(VendorID),
    primary key (ProductNumber, VendorID)
);


CREATE TABLE Products (
	ProductNumber int NOT NULL primary key,
	ProductName text NULL ,
	ProductDescription text NULL ,
	RetailPrice decimal NULL ,
	QuantityOnHand smallint NULL ,
	CategoryID int NULL,
    foreign key (CategoryID) references Categories(CategoryID)
);


CREATE TABLE Vendors (
	VendorID int NOT NULL primary key ,
	VendName text NULL ,
	VendStreetAddress text NULL ,
	VendCity text NULL ,
	VendState text NULL ,
	VendZipCode text NULL ,
	VendPhoneNumber text NULL ,
	VendFaxNumber text NULL ,
	VendWebPage text NULL ,
	VendEMailAddress text NULL 
); 







