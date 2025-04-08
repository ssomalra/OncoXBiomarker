CREATE DATABASE final_project;
USE final_project;
SHOW tables; 

CREATE TABLE Biomarker (
biomarker_id CHAR(4) NOT NULL PRIMARY KEY,
gene_symbol VARCHAR(30),
gene_full_name VARCHAR(100),
gene_function LONGTEXT
);

CREATE TABLE Cancer (
cancer_id CHAR(4) NOT NULL PRIMARY KEY,
cancer_name VARCHAR(30),
subtype_name TEXT,
ICD VARCHAR(30),
cancer_description LONGTEXT
);

CREATE TABLE Biomarker_Impact (
impact_id CHAR(6) NOT NULL PRIMARY KEY,
biomarker_id CHAR(4) NOT NULL,
cancer_id CHAR(4) NOT NULL,
biomarker_role TEXT,
mutation_type TEXT,
clinical_implication TEXT,
pathway_involvement LONGTEXT,
treatment TEXT,
FOREIGN KEY (biomarker_id) REFERENCES Biomarker (biomarker_id) ON DELETE CASCADE,
FOREIGN KEY (cancer_id) REFERENCES Cancer (cancer_id) ON DELETE CASCADE
);

CREATE TABLE Ref (
reference_id INT PRIMARY KEY NOT NULL,
URL TEXT,
title TEXT,
source VARCHAR(300),
publication_year YEAR,
primary_author VARCHAR(100)
);

CREATE TABLE Biomarker_Impact_Reference (
impact_id CHAR(6) NOT NULL,
reference_id INT NOT NULL,
PRIMARY KEY (impact_id, reference_id), 
FOREIGN KEY (impact_id) REFERENCES Biomarker_Impact(impact_id) ON DELETE CASCADE,
FOREIGN KEY (reference_id) REFERENCES Ref(reference_id) ON DELETE CASCADE
);

/* to load data in TSV files into SQL tables
1. open terminal
2. mysql --local-infile=1 -u root -p
   USE final_project;
   LOAD DATA LOCAL INFILE '~/Documents/IUPUI/24-25 Courses/Database/FinalProject/django/Biomarker.tsv' INTO TABLE Biomarker FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
   LOAD DATA LOCAL INFILE '~/Documents/IUPUI/24-25 Courses/Database/FinalProject/django/Cancer.tsv' INTO TABLE Cancer FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
   LOAD DATA LOCAL INFILE '~/Documents/IUPUI/24-25 Courses/Database/FinalProject/django/Reference.tsv' INTO TABLE Ref FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
   LOAD DATA LOCAL INFILE '~/Documents/IUPUI/24-25 Courses/Database/FinalProject/django/Biomarker_Impact.tsv' INTO TABLE Biomarker_Impact FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
   LOAD DATA LOCAL INFILE '~/Documents/IUPUI/24-25 Courses/Database/FinalProject/django/Biomarker_Impact_Reference.tsv' INTO TABLE Biomarker_Impact_Reference FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
*/

SELECT * FROM Biomarker;
SELECT * FROM Cancer;
SELECT * FROM Biomarker_Impact;
SELECT * FROM Ref;
SELECT * FROM Biomarker_Impact_Reference;

DROP TABLE Biomarker_Impact_Reference;
DROP TABLE Biomarker_Impact;
#DROP TABLE Biomarker;
DROP TABLE Cancer;
DROP TABLE Ref;