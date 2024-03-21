INSERT INTO VAT (VAT_ID, Country, Country_Code, VAT_Rate) VALUES
(1, 'Austria', 'AT', 20.00),
(2, 'Belgium', 'BE', 21.00),
(3, 'Bulgaria', 'BG', 20.00),
(4, 'Croatia', 'HR', 25.00),
(5, 'Cyprus', 'CY', 19.00),
(6, 'Czech Republic', 'CZ', 21.00),
(7, 'Denmark', 'DK', 25.00),
(8, 'Estonia', 'EE', 20.00),
(9, 'Finland', 'FI', 24.00),
(10, 'France', 'FR', 20.00),
(11, 'Germany', 'DE', 19.00),
(12, 'Greece', 'GR', 24.00),
(13, 'Hungary', 'HU', 27.00),
(14, 'Ireland', 'IE', 23.00),
(15, 'Italy', 'IT', 22.00),
(16, 'Latvia', 'LV', 21.00),
(17, 'Lithuania', 'LT', 21.00),
(18, 'Luxembourg', 'LU', 17.00),
(19, 'Malta', 'MT', 18.00),
(20, 'Netherlands', 'NL', 21.00),
(21, 'Poland', 'PL', 23.00),
(22, 'Portugal', 'PT', 23.00),
(23, 'Romania', 'RO', 19.00),
(24, 'Slovakia', 'SK', 20.00),
(25, 'Slovenia', 'SI', 22.00),
(26, 'Spain', 'ES', 21.00),
(27, 'Sweden', 'SE', 25.00);

INSERT INTO Discount (Discount_ID, Discount_Name, Discount_Rate, OrderValue) VALUES
(1, '3% off', 3.00, 1000.00),
(2, '5% off', 5.00, 5000.00),
(3, '10% off', 10.00, 10000.00);

INSERT INTO Orders (order_id, item_name, quantity, unit_price, sub_total_price, vat_price, discount_price, total_price, vat_id, discount_id) VALUES
(1001, 'item 1', 1, 100, 0, 0, 0, 5, 1),
(1002, 'item 2', 10, 20, 0, 0, 0, 10, 2),
(1003, 'item 3', 120, 30, 0, 0, 0, 7, 3);