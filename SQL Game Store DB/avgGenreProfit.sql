CREATE DEFINER=`root`@`localhost` FUNCTION `avgGenreProfit`(genreGames varchar(255)) RETURNS int
    DETERMINISTIC
BEGIN
	declare avg1 int;
    select sum(gamePrice*gamesSold-developmentCost)/count(gamePrice) into avg1 from Games where genreGames like concat("%",gameName,"%");
RETURN avg1;
END