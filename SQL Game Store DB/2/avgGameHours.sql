CREATE DEFINER=`root`@`localhost` FUNCTION `avgGameHours`(gameName varchar(255)) RETURNS int
    DETERMINISTIC
BEGIN
	declare avg1 int;
    select sum(hoursPlayed)/count(*) into avg1 from Players where playerGames like concat("%",gameName,"%");
RETURN avg1;
END