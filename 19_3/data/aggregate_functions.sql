--SELECT SUM(Quantity) FROM Sales;

--SELECT COUNT(*) FROM Employees;

--SELECT DepartmentID,COUNT(*) FROM Employees GROUP BY DepartmentID;


--SELECT D.DepartmentName, COUNT(*) AS Employees
-- FROM Employees AS e  INNER JOIN Departments AS D
--ON e.DepartmentID = D.DepartmentID
--GROUP BY D.DepartmentID ;


--SELECT count(NickName) FROM Employees;


--SELECT r.RegionName, SUM(s.Quantity) FROM Sales AS s
--   INNER JOIN Regions as r ON r.RegionID = s.RegionID
--   GROUP BY r.RegionID;


--SELECT P.ProductName,SUM(s.Quantity) FROM Sales AS s
--   INNER JOIN Products AS P ON P.ProductID = s.ProductID
--   GROUP BY p.ProductID;


SELECT P.ProductName,COUNT(s.Quantity) FROM Sales AS s
   INNER JOIN Products AS P ON P.ProductID = s.ProductID
   GROUP BY p.ProductID;