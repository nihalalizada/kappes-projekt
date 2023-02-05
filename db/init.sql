CREATE DATABASE projekt;
use projekt;

CREATE TABLE accounts (
  id INT  AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  iban VARCHAR(255),
  amount VARCHAR(255),
  purpose VARCHAR(255)
);

INSERT INTO accounts
  (name, iban, amount, purpose)
VALUES
  ('Nihal', 'DE12345xxx', '599', 'Miete'),
  ('r00t', 'DE12345xxx', '199', 'Versicherung');

CREATE TABLE admins (
  id INT  AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE logins (
  id INT  AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255)
);

INSERT INTO admins
(username, password) 
VALUES
('nihal','user'),
('ali', 'admin'),
('nik', 'user');