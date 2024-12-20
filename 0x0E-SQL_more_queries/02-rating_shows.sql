--  creates the database hbtn_0d_2 and the user user_0d_2.

SELECT tv_shows.title, sum(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
