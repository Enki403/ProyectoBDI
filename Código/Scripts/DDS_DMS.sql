DROP DATABASE IF EXISTS testUser;
CREATE DATABASE testUser;
USE testUser;

CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    password VARCHAR(50) NOT NULL,
    creationDate DATE NOT NULL,
    modificationDate TIMESTAMP DEFAULT NOW()
);

INSERT INTO User(name,password,creationDate) VALUES 
    ('Nelson Sambula','nel','2020-04-11'),
    ('Leonel Messi','ja','2020-03-23'),
    ('Crsitiano Ronaldo','je','2020-07-19')
;

SELECT * FROM User;
