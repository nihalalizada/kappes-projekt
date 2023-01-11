CREATE DATABASE projekt;
use projekt;

CREATE TABLE accounts (
  id VARCHAR(255) PRIMARY KEY AUTO_INCREMENT,
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