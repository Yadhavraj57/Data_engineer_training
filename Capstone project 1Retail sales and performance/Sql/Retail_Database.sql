 
CREATE DATABASE IF NOT EXISTS retail_db;
USE retail_db;

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    stock_qty INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stores (
    store_id INT PRIMARY KEY AUTO_INCREMENT,
    store_name VARCHAR(150) NOT NULL,
    region VARCHAR(100),
    city VARCHAR(100),
    manager_id INT,
    opened_date DATE
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(150) NOT NULL,
    store_id INT,
    role VARCHAR(80),
    salary DECIMAL(10,2),
    hire_date DATE,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    emp_id INT,
    quantity INT NOT NULL DEFAULT 1,
    sale_price DECIMAL(10,2) NOT NULL,
    discount_pct DECIMAL(5,2)  DEFAULT 0.00,
    sale_date DATE NOT NULL,
    FOREIGN KEY (store_id)   REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (emp_id)     REFERENCES employees(emp_id)
);

INSERT INTO stores (store_name, region, city, opened_date) VALUES
  ('Chennai Central',  'South', 'Chennai',  '2020-01-15'),
  ('Mumbai Flagship',  'West',  'Mumbai',   '2019-06-01'),
  ('Delhi North Hub',  'North', 'Delhi',    '2021-03-20'),
  ('Bangalore Tech',   'South', 'Bangalore','2022-07-10'),
  ('Kolkata East',     'East',  'Kolkata',  '2020-11-05');
 
INSERT INTO products (product_name, category, price, cost, stock_qty) VALUES
  ('Smart TV 55"',     'Electronics', 45000.00, 32000.00, 50),
  ('Running Shoes',    'Footwear',     3500.00,  1800.00, 200),
  ('Coffee Maker',     'Appliances',   5200.00,  3100.00,  80),
  ('Laptop 14" i5',   'Electronics', 62000.00, 48000.00,  30),
  ('Yoga Mat',         'Sports',        950.00,   400.00, 150),
  ('Dinner Set 12pc',  'Kitchen',      2800.00,  1500.00,  60);
 
INSERT INTO employees (emp_name, store_id, role, salary, hire_date) VALUES
  ('Arjun Mehta',   1, 'Store Manager',  55000.00, '2020-01-15'),
  ('Priya Sharma',  1, 'Sales Executive',28000.00, '2021-03-01'),
  ('Karan Patel',   2, 'Store Manager',  52000.00, '2019-06-01'),
  ('Sneha Reddy',   2, 'Sales Executive',26000.00, '2022-01-10'),
  ('Vikram Singh',  3, 'Store Manager',  54000.00, '2021-03-20');
  
INSERT INTO sales (store_id, product_id, emp_id, quantity, sale_price, discount_pct, sale_date) VALUES
  (1, 1, 1,  2, 44000.00, 2.22, '2024-01-10'),
  (2, 2, 3,  5,  3500.00, 0.00, '2024-01-11'),
  (1, 3, 2,  1,  5000.00, 3.85, '2024-01-12'),
  (3, 4, 5,  1, 61000.00, 1.61, '2024-01-13'),
  (2, 5, 4, 10,   950.00, 0.00, '2024-01-14'),
  (4, 6, 1,  3,  2800.00, 0.00, '2024-01-15');  
  
  
  SELECT
    s.store_name,s.region, p.product_name,
    p.category,sa.quantity,sa.sale_price,sa.discount_pct,ROUND(sa.quantity * sa.sale_price, 2) AS revenue, ROUND(sa.quantity * (sa.sale_price - p.cost), 2) AS profit
FROM sales sa
JOIN stores   s ON sa.store_id   = s.store_id
JOIN products p ON sa.product_id = p.product_id
ORDER BY revenue DESC;

SELECT s.store_name, s.region, SUM(sa.quantity * sa.sale_price) AS total_revenue,SUM(sa.quantity * (sa.sale_price - p.cost))  AS total_profit,
COUNT(sa.sale_id) AS transactions, SUM(sa.quantity) AS units_sold
FROM sales sa
JOIN stores   s ON sa.store_id   = s.store_id
JOIN products p ON sa.product_id = p.product_id
GROUP BY s.store_id, s.store_name, s.region
ORDER BY total_revenue DESC;

UPDATE products SET price = 21000 WHERE product_name = 'Phone';
DELETE FROM products WHERE product_name = 'Shirt';

UPDATE products
SET price = ROUND(price * 0.95, 2)
WHERE category = 'Electronics';

DELIMITER //

CREATE PROCEDURE GetDailySales(IN storeId INT, IN saleDate DATE)
BEGIN
    SELECT 
        s.store_name,
        SUM(sa.quantity * sa.sale_price) AS total_sales
    FROM sales sa
    JOIN stores s ON sa.store_id = s.store_id
    WHERE sa.store_id = storeId AND sa.sale_date = saleDate
    GROUP BY s.store_name;
END //

DELIMITER ;

CALL GetDailySales(1, '2025-01-01');

CREATE INDEX idx_product ON products(product_name);
CREATE INDEX idx_region ON stores(region);

SELECT 
    s.store_name,
    SUM(sa.quantity * sa.sale_price) AS revenue
FROM sales sa
JOIN stores s ON sa.store_id = s.store_id
GROUP BY s.store_name;

SELECT 
    p.product_name,
    SUM(sa.quantity) AS total_sold
FROM sales sa
JOIN products p ON sa.product_id = p.product_id
GROUP BY p.product_name
HAVING total_sold < 3;