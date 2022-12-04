CREATE DATABASE students;
use students;

CREATE TABLE users (
  id VARCHAR(20),
  name VARCHAR(10)
);

INSERT INTO users
  (id, name)
VALUES
  ('1', 'Nihal'),
  ('2', 'r00t');