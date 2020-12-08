DROP DATABASE IF EXISTS testUser;
CREATE DATABASE testUser;
USE testUser;

CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    username VARCHAR(200),
    password VARCHAR(50) NOT NULL,
    creationDate DATE DEFAULT NOW(),
    modificationDate TIMESTAMP DEFAULT NOW()
);

INSERT INTO User(name,password,creationDate,username) VALUES 
    ('Nelson Sambula','contra123','2020-04-11','nelsinho10'),
    ('Leonel Messi','00dificil','2020-03-23','la pulga'),
    ('Crsitiano Ronaldo','siuuuu','2020-07-19','el bicho')
;

INSERT INTO User(name,password,username) VALUES 
    ('Renata Dubon','renata987','import re'),
    ('Hector Vasquez','hector123','enki'),
    ('Luis Gutierrez','luis222','mrzombie')
;
SELECT * FROM User;
