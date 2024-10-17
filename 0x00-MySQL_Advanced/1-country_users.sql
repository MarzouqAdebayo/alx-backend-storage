-- Creates a table users with id, email, name, country
DROP TABLE IF NOT EXISTS users;
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country CHAR(2) NOT NULL DEFAULT 'US' CHECK (COUNTRY IN ('US', 'CO', 'TN'))
);
