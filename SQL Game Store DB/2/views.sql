

create or replace view mostProfitableGame as
select gameName, gamePrice*gamesSold-developmentCost as "profit in millions" from games
order by gamePrice*gamesSold-developmentCost desc limit 10;



create or replace view mostPopularGames as
select gameName, gamesSold from games
order by gamesSold desc limit 10;


create or replace view shortestDevelopmentTimeGame as
select gameName, datediff(releaseDate, developmentDate) as days from Games
order by datediff(releaseDate, developmentDate) desc limit 10;


create or replace view earliestGameGenres as
select genreName, creationDate from Genres
order by creationDate desc limit 10;


create or replace view earliestGamePlatforms as
select platformName, creationDate from Platforms
order by creationDate desc limit 10;

create or replace view earliestGameCompanies as
select companieName, creationDate from Companies
order by creationDate desc limit 10;


create or replace view mostProfitableGenres as
select genreName, avgGenreProfit(genreGames) from Genres
order by avgGenreProfit(genreGames) desc;


create or replace view avgGenresPrice as
select genreName, avgGenrePrice(genreGames) from Genres
order by avgGenrePrice(genreGames);



create or replace view mostUnusedGenres as
select genreName, 1+length(genreGames)-length(REPLACE(genreGames, ',', '')) as "count" from Genres
order by 1+length(genreGames)-length(REPLACE(genreGames, ',', '')) limit 10;


create or replace view mostProfitablePlatforms as
select platformName, avgPlatformProfit(platformGames) from Platforms
order by avgPlatformProfit(platformGames) desc limit 10;


create or replace view mostProfitableCompanies as
select companieName, avgCompanyProfit(companyGames) from Companies
order by avgCompanyProfit(companyGames) desc limit 10;


create or replace view mostAccessiblePlatforms as
select platformName, platformPrice from Platforms
order by platformPrice limit 10;


create or replace view mostHardcorePlayers as
select playerName, hoursPlayed from Players
order by hoursPlayed desc limit 10;

create or replace view mostHardcoreGamePlayerBases as
select gameName, avgGameHours(gameName) from Games
order by avgGameHours(gameName) desc limit 10;

create or replace view mostHardcoreGenrePlayerBases as
select genreName, avgGenreHours(genreGames) from Genres
order by avgGenreHours(genreGames) desc limit 10;