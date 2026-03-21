--SELECT artists.name AS Artist, albums.name AS Album, s.track, s.title
-- FROM songs AS s
--      INNER JOIN albums ON s.album = albums._id
--      INNER JOIN artists ON albums.artist = artists._id
--      WHERE s.title LIKE '%doctor%'
--      ORDER BY Artist, Album, s.track;


--SELECT songs.title, artists.name FROM songs
--        INNER JOIN albums ON songs.album = albums._id
--        INNER JOIN artists ON albums.artist = artists._id
--        WHERE artists.name LIKE 'Vlad_mir V_sotsk_';



SELECT * FROM songs
    WHERE title like 'American%';