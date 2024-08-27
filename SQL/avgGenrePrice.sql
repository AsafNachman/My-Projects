CREATE FUNCTION `avgGenrePrice` (genreGames varchar(255)) RETURNS int
    DETERMINISTIC
BEGIN
	declare avg1 int;
    select sum(gamePrice)/count(gamePrice) into avg1 from Games where genreGames like concat("%",gameName,"%");
RETURN avg1;
END
