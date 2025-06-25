-- List shows with their genre IDs, sorted by show title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;