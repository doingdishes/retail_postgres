csv grabbed from
https://www.kaggle.com/datasets/roopacalistus/superstore?resource=download

this project grabs information from a locally stored PostGreSQL database. the data set supplied is stored into this database as a table. 

multiple libraries are utilized to transform the data for analysis and/or visualization.

table management was done with psql. the csv included in this directory was loaded into the database by 1) creating a table with the correct column names and 2) importing the csv with \copy. postgres enables the creation of automatic serialized primary keys. this was utilized since our stores were not serialized.

the database is named after the csv (sample_superstore). the table is imported as retail_stores using the following script in psql:

CREATE TABLE retail_stores (
    id SERIAL PRIMARY KEY,
    ship_mode TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT,
    category TEXT,
    sub_category TEXT,
    sales NUMERIC(10,2),
    quantity INTEGER,
    discount NUMERIC(4,2),
    profit NUMERIC(10,2)
);

then, we used the following to copy the information from the csv into the database:

\copy retail_stores(ship_mode, segment, country, city, state, postal_code, region, category, sub_category, sales, quantity, discount, profit)
FROM 'path to csv' DELIMITER ',' CSV HEADER;

alternatively, one could use the function from importcsv.py to import a csv to the database if they do not want to work in psql. this method is not recommended as it is generally slower than using psql, especially if the csv is large.

there is another module for converting excel workbooks to csv using pandas and openpyxl. this is under transformations.py