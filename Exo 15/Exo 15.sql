-- Etape 1


CREATE TABLE apprenants (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(200) NOT NULL,
  last_name varchar(200) NOT NULL
);
  
CREATE TABLE encadrants(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(200) NOT NULL,
    last_name varchar(200) NOT NULL
);

INSERT INTO apprenants(first_name, last_name)
    VALUES ('Kevin', 'Cheron'),
    ('Audrey', 'Djibilian');

INSERT INTO encadrants(first_name, last_name)
    VALUES ('Fred', 'Arnoux');


    -- SELECT * FROM apprenants;
    -- SELECT last_name AS nom, first_name AS prenom FROM encadrants;

-- Etape 2

    -- SELECT last_name, first_name, 'encadrant' AS type FROM encadrants
    -- UNION
    -- SELECT last_name, first_name, 'apprenant' AS type FROM apprenants;

-- Etape 3


CREATE TABLE promotions(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(200) NOT NULL,
  month_year varchar(200) NOT NULL,
  UNIQUE KEY (month_year)
);
  
INSERT INTO promotions(name, month_year)
VALUES ('Doria Shafik', 'janvier 2023'),
  ('Dorothy Vaughan', 'octobre 2022');
  
CREATE TABLE promotions_apprenants(
  promotions_id INT NOT NULL, 
  apprenants_id INT NOT NULL,
  FOREIGN KEY (promotions_id) REFERENCES promotions (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (apprenants_id) REFERENCES apprenants (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  PRIMARY KEY (promotions_id, apprenants_id)
);

INSERT INTO promotions_apprenants (promotions_id, apprenants_id)
VALUES (1, 1),
  (2,2);


    -- SELECT first_name, last_name, name AS promotion, month_year AS Rentree
    -- FROM apprenants
    -- JOIN promotions_apprenants ON apprenants.id = promotions_apprenants.apprenants_id
    -- JOIN promotions ON promotions.id = promotions_apprenants.promotions_id;

-- Etape 4

CREATE TABLE apprenants (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(200) NOT NULL,
  last_name varchar(200) NOT NULL
);
  
CREATE TABLE encadrants(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(200) NOT NULL,
  last_name varchar(200) NOT NULL
);
    
INSERT INTO apprenants(first_name, last_name)
VALUES ('Kevin', 'Cheron'),
  ('Elsa', 'Catoire'),
  ('Oumaima', 'Lamrabat'),
  ('Cindy', 'Bestaven'),
  ('Audrey', 'Djibilian');
    
INSERT INTO encadrants(first_name, last_name)
VALUES ('Fred', 'Arnoux');
    
CREATE TABLE promotions(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(200) NOT NULL,
  year varchar(200) NOT NULL
);
  
INSERT INTO promotions(name, year)
VALUES ('Doria Shafik', '2023'),
  ('Dorothy Vaughan', '2022'),
  ('Doris Stauffer', '2023');
  
CREATE TABLE promotions_apprenants(
  promotions_id INT NOT NULL, 
  apprenants_id INT NOT NULL,
  FOREIGN KEY (promotions_id) REFERENCES promotions (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (apprenants_id) REFERENCES apprenants (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  PRIMARY KEY (promotions_id, apprenants_id)
);

INSERT INTO promotions_apprenants (promotions_id, apprenants_id)
VALUES (1, 1),
  (2, 5),
  (1, 2),
  (1, 3),
  (2, 4);

    -- SELECT first_name, last_name, name AS promotion, year AS Rentree
    -- FROM apprenants
    -- JOIN promotions_apprenants ON apprenants.id = promotions_apprenants.apprenants_id
    -- JOIN promotions ON promotions.id = promotions_apprenants.promotions_id
    -- WHERE promotions.name = 'Doria Shafik';



    -- SELECT name FROM promotions
    -- WHERE year = '2023';