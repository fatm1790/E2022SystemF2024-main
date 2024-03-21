create database OrderDB;
use OrderDB;

CREATE TABLE IF NOT EXISTS VAT (
    VAT_ID INT PRIMARY KEY,
    Country VARCHAR(255),
    Country_Code CHAR(2),
    VAT_Rate DECIMAL(5, 2)
);
drop table vat;
                       
CREATE TABLE IF NOT EXISTS Discount (
    Discount_ID INT PRIMARY KEY,
    Discount_Name VARCHAR(255),
    Discount_Rate DECIMAL(5, 2),
    OrderValue DECIMAL(10, 2)
);
                       
drop table discount;                       
                       
CREATE TABLE IF NOT EXISTS orders
                      (order_id INTEGER PRIMARY KEY, 
                       item_name TEXT,
                       quantity INTEGER,
                       unit_price REAL,
                       sub_total_price REAL,
                       vat_price REAL,
                       discount_price REAL,
                       total_price REAL,
                       vat_id INTEGER,
                       discount_id INTEGER,
                       FOREIGN KEY (vat_id) REFERENCES vat(vat_id),
                       FOREIGN KEY (discount_id) REFERENCES discount(discount_id));   
                       
drop table orders;                       