SELECT  name, country, numguns, launched  FROM ships 
  JOIN classes ON ships.class = classes.class;

SELECT classes.class, name, country, numguns, launched FROM classes   
  LEFT join ships ON ships.class = classes.class;

SELECT ship FROM outcomes 
  JOIN battles ON battles.name = outcomes.battle 
  WHERE DATE LIKE "1942-%%-%%"; 

SELECT classes.country, name FROM ships 
  JOIN classes ON classes.class = ships.class 
  LEFT join outcomes ON ships.name = outcomes.ship 
  WHERE battle IS NULL; 