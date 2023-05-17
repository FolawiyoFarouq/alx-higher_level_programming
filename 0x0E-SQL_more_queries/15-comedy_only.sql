-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- F A R O U8 Q
SELECT tv_shows.title AS title
FROM tv_shows
     JOIN tv_show_genres
     	  ON tv_show_genres.show_id = tv_shows.id
     JOIN tv_genres
     	  ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;