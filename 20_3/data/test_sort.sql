--SELECT * FROM artists;

--SELECT * FROM artists ORDER BY name;

--SELECT * FROM albums ORDER BY name;


--SELECT * FROM albums ORDER BY name COLLATE NOCASE DESC;

--SELECT * FROM albums
--  WHERE artist = 72
--  ORDER BY name COLLATE NOCASE ASC;


SELECT * FROM songs ORDER BY album,track;