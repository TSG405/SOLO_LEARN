'''
@Coded by TSG, 2021

Problem:


You manage a zoo. Each animal in the zoo comes from a different country. Here are the tables you have:
Animals
https://api.sololearn.com/DownloadFile?id=4534

Countries
https://api.sololearn.com/DownloadFile?id=4533

1) A new animal has come in, with the following details:
name - "Slim", type - "Giraffe", country_id - 1
Add him to the Animals table.
2) You want to make a complete list of the animals for the zoo’s visitors. Write a query to output a new table with each animal's name, type and country fields, sorted by countries.
'''



/*CODE*/
INSERT INTO Animals VALUES ('Slim','Giraffe', 1);

SELECT a.name,a.type,c.country
FROM Animals AS a INNER JOIN Countries AS c
ON a.country_id = c.id
ORDER BY c.country;
