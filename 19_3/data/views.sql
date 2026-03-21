--CREATE VIEW artist_list1 AS
--SELECT artists.name, albums.name, songs.track, songs.title
--     FROM songs INNER JOIN albums ON songs.album = albums._id
--     INNER JOIN artists ON albums.artist = artists._id
--     ORDER BY artists.name, albums.name, songs.track;


--SELECT * FROM artist_list1 WHERE name LIKE 'jefferson%';

--CREATE VIEW album_list AS SELECT name FROM albums ORDER BY name COLLATE NOCASE;

--SELECT * FROM album_list;

--SELECT * FROM sqlite_schema WHERE name = 'artist_list1';

--DROP VIEW album_list;

--DROP view artist_list1;

--CREATE VIEW artist_list1 AS 
--SELECT artists.name AS Artist, albums.name AS Album, songs.track, songs.title FROM songs 
--         INNER JOIN albums ON songs.album = albums._id
--         INNER JOIN artists ON albums.artist = artists._id 
--         ORDER BY Artist COLLATE NOCASE, Album COLLATE NOCASE, songs.track;

SELEC
