CREATE DATABASE projekt;
use projekt;

CREATE TABLE accounts (
  id VARCHAR(255) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255),
  iban VARCHAR(255),
  amount VARCHAR(255),
  purpose VARCHAR(255)
);

INSERT INTO accounts
  (id, name, iban, amount, purpose)
VALUES
  ('1', 'Nihal', 'DE12345xxx', '599', 'Miete'),
  ('2', 'r00t', 'DE12345xxx', '199', 'Versicherung');

  CREATE TABLE admin (
  id VARCHAR(255) NOT NULL AUTO_INCREMENT,
  username VARCHAR(255),
  password VARCHAR(255)
);

INSERT INTO admin
(id, username, password) 
VALUES
('1', 'nihal','user'),
('2', 'ali', 'admin');