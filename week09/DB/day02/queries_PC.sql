SELECT avg(speed) FROM laptop;

SELECT avg(screen), maker 
  FROM laptop 
  JOIN product ON laptop.model = product.model 
  GROUP BY maker; 

SELECT avg(speed) FROM laptop WHERE price > 1000;

SELECT avg(price), hd 
  FROM laptop 
  JOIN product ON laptop.model = product.model 
  GROUP BY hd; 

SELECT avg(price), maker  
  FROM pc 
  INNER JOIN product ON product.model=pc.model 
  WHERE speed > 500 
  GROUP BY maker;

SELECT avg(price) 
  FROM pc 
  INNER JOIN product ON product.model=pc.model 
  WHERE maker = "A" 
  GROUP BY maker;

SELECT avg(price) 
  FROM pc 
  INNER JOIN product ON product.model=pc.model 
  WHERE maker = "B" 
  GROUP BY maker; 
  
----- 8 ----
------------
------------
------------
------------
------------
SELECT * 
  FROM pc 
  ORDER by price DESC 
  LIMIT 1;

---  10 --- 
-----------
-----------
-----------
-----------
-----------