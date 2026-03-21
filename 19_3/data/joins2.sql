--SELECT artists.name AS Artist, albums.name AS Album, songs.track, songs.title FROM songs
--     INNER JOIN albums ON songs.album = albums._id
--     INNER  JOIN artists ON albums.artist = artists._id
--     ORDER BY Artist, Album, songs.track;

SELECT artists.name AS Artist, albums.name AS Album, s.track, s.title
 FROM songs AS s
      INNER JOIN albums ON s.album = albums._id
      INNER JOIN artists ON albums.artist = artists._id
      WHERE albums._id = 20
      ORDER BY Artist, Album, s.track;