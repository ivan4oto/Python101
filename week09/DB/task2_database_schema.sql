----- First Queries ----- 

SELECT address FROM STUDIO
WHERE name='MGM';

SELECT birthdate FROM MOVIESTAR
WHERE name = 'Kim Basinger';

SELECT name FROM MOVIEEXEC
WHERE networth > 10000000;

SELECT name FROM MOVIESTAR
WHERE gender = "M" or address = "Perfect Rd.";

INSERT into MOVIESTAR
VALUES ("Zahari Baharov", "Fakulteta Hills", "M", "1980-08-12");

DELETE from STUDIO
WHERE address LIKE "%5%"; 

UPDATE MOVIE
SET studioname = 'Fox'
WHERE title LIKE "%star%";

----- Relations -----

SELECT STARSIN.starname
FROM STARSIN
INNER JOIN MOVIESTAR ON MOVIESTAR.name=STARSIN.STARNAME
WHERE STARSIN.MOVIETITLE = "Terms of Endearment" and MOVIESTAR.gender = "M";

SELECT STARSIN.starname
FROM STARSIN
INNER JOIN MOVIE ON MOVIE.title=STARSIN.MOVIETITLE
WHERE MOVIE.studioname = "MGM" and year = 1995;

UPDATE STUDIO
SET "president name" = "Chris Brearton"
WHERE Name = "MGM"; 

UPDATE STUDIO
SET "president name" = "Kondio"
WHERE Name = "USA Entertainm."; 

SELECT "president name" FROM STUDIO
WHERE Name = "MGM"; 