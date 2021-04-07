'''
@Coded by TSG, 2021

Problem:


A local bakery creates unique cake sets. Each cake set contains three different cakes.
Here is the cakes table:
https://api.sololearn.com/DownloadFile?id=4530

Тoday a customer want a cake set that has minimal calories.
Write a query to sort the cakes by calorie count and select the first 3 cakes from the list to offer the customer.
'''



/*CODE*/
SELECT DISTINCT name, calories FROM Cakes
ORDER BY calories LIMIT 3;
