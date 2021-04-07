'''
@Coded by TSG, 2021

Problem:


You want to rent an apartment and have the following table named Apartments:
https://api.sololearn.com/DownloadFile?id=4535

Write a query to output the apartments whose prices are greater than the average and are also not rented, sorted by the 'Price' column.
'''



/*CODE*/
SELECT * FROM Apartments
WHERE price > (SELECT AVG(price) FROM Apartments) AND status='Not rented'
ORDER BY price;
