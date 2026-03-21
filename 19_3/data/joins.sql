--SELECT track,title,name FROM songs
--   JOIN albums ON album = albums._id;

--SELECT songs.track, songs.title, albums.name FROM songs
--      JOIN albums ON songs.album = albums._id;


--SELECT * FROM songs
--     JOIN albums ON songs.album = albums._id
--     ORDER BY albums._id, songs.track;


--SELECT albums.name, songs.track, songs.title, songs.album, albums._id
--FROM songs INNER JOIN albums ON songs.album = albums._id;


SELECT artists.name, albums.name FROM artists 
     INNER JOIN albums ON albums.artist = artists._id                                                    ORDER BY artists.name;