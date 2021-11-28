import sqlparse

from SQL_Parser import format_query

query1 = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway')"


query2= "select SUM(height) as total_height, AVG(height) as average_height FROM (SELECT id, height FROM person GROUP BY id, height) WHERE height>100 AND weight<50"


query3="UPDATE Database SET Name='Anant' WHERE Database.Id=50;"


query4="SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID"


print(format_query(query1), end='\n\n')

print(format_query(query2), end='\n\n')

print(format_query(query3), end='\n\n')

print(format_query(query4), end='\n\n')


