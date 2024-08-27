
drop database if exists main;

create database main;

use main;

create table Games(
gameName varchar(255),
gamePrice int, # dollar
gamesSold int, # million
developmentDate date,
releaseDate date,
developmentCost int # million
);

insert into Games(gameName, gamePrice, gamesSold, developmentDate, releaseDate, developmentCost)
values("Elden Ring", 60, 20, '2017-3-29', '2022-2-25', 200),
("Rocket League", 20, 40, "2013-1-1", '2015-7-7', 2),
("Among Us", 5, 3.2, "2017-11-1",'2018-8-1', 15),
("Hogwarts Legacy", 60, 12, "2017-1-1",'2023-2-7', 150),
("Cyberpunk 2077", 60, 20, '2016-5-1', '2020-12-10', 174),
("Grand Theft Auto V", 60, 175, '2008-1-1', '2013-9-17', 137),
("Call of Duty: Black Ops III", 60, 26.72, '2012-1-1', '2015-11-5', 23),
("Five Nights at Freddy's: Security Breach", 40, 42.2, '2020-1-1', '2021-12-16', 2),
("Red Dead Redemption 2", 60, 50, '2010-5-19', '2018-10-26', 644),
("Monster Hunter World", 50, 20, '2015-1-1', '2018-1-26', 60),
("Plants vs. Zombies", 30, 9, '2006-1-1', '2009-5-5', 30),
("Forza Horizon 5", 60, 15, "2018-1-1", "2021-11-5", 60),
("Skylanders Spyro's Adventure", 70, 30, '2009-6-1', '2011-10-16', 100);


create table Genres(
genreName varchar(255),
creationDate year,
genreGames varchar(255)
);

insert into Genres(genreName, creationDate, genreGames)
values("Action", "1979", "Forza Horizon 5, Monster Hunter World, Elden Ring, Among Us, Hogwarts Legacy, Cyberpunk 2077, Grand Theft Auto V, Call of Duty: Black Ops III, Five Nights at Freddy's: Security Breach, Red Dead Redemption 2, Skylanders Spyro's Adventure"),
("Adventure", "1976", "Skylanders Spyro's Adventure, Forza Horizon 5, Monster Hunter World, Elden Ring, Hogwarts Legacy, Cyberpunk 2077, Grand Theft Auto V, Five Nights at Freddy's: Security Breach, Red Dead Redemption 2"),
("Fantasy", "1980", "Skylanders Spyro's Adventure, Monster Hunter World, Elden Ring, Hogwarts Legacy"),
("Open World", "1986", "Forza Horizon 5, Monster Hunter World, Elden Ring, Hogwarts Legacy, Cyberpunk 2077, Grand Theft Auto V, Red Dead Redemption 2"),
("Singerplayer", "1958", "Skylanders Spyro's Adventure, Forza Horizon 5, Monster Hunter World, Elden Ring, Hogwarts Legacy, Cyberpunk 2077, Grand Theft Auto V, Call of Duty: Black Ops III, Five Nights at Freddy's: Security Breach, Red Dead Redemption 2"),
("Rpg", "1980", "Skylanders Spyro's Adventure, Elden Ring, Hogwarts Legacy, Cyberpunk 2077, Monster Hunter World"),
("Racing", "1972", "Forza Horizon 5, Rocket League, Grand Theft Auto V"),
("Mulitplayer", "1973", "Skylanders Spyro's Adventure, Forza Horizon 5, Monster Hunter World, Rocket League, Among Us, Grand Theft Auto V, Call of Duty: Black Ops III, Red Dead Redemption 2"),
("Competitive/Pvp", "1991", "Forza Horizon 5, Rocket League, Call of Duty: Black Ops III"),
("Sports", "1958", "Rocket League, Grand Theft Auto V, Forza Horizon 5"),
("Casual", "1990", "Among Us, Rocket League"),
("Survival", "1992", "Among Us, Five Nights at Freddy's: Security Breach"),
("Shooter", "1973", "Cyberpunk 2077, Grand Theft Auto V, Call of Duty: Black Ops III, Red Dead Redemption 2"),
("Crime", 2003, "Red Dead Redemption 2, Cyberpunk 2077, Grand Theft Auto V"),
("Story Rich", 1981, "Red Dead Redemption 2, Cyberpunk 2077, Grand Theft Auto V, Call of Duty: Black Ops III, Five Nights at Freddy's: Security Breach"),
("Difficult", 2015, "Monster Hunter World, Elden Ring");



create table Platforms(
platformName varchar(255),
platformPrice int,
creationDate year,
platformGames varchar(255)
);

insert into Platforms(platformName, platformPrice, creationDate, platformGames)
values("PC", 1000, "1971", "Skylanders Spyro's Adventure, Forza Horizon 5, Monster Hunter World, Red Dead Redemption 2, Elden Ring, Rocket League, Among Us, Hogwarts Legacy, Cyberpunk 2077, Grand Theft Auto V, Call of Duty: Black Ops III"),
("PlayStation 4", 250, "2013", "Plants vs. Zombies, Monster Hunter World, Red Dead Redemption 2, Five Nights at Freddy's: Security Breach, Call of Duty: Black Ops III, Grand Theft Auto V, Elden Ring, Rocket League, Among Us, Hogwarts Legacy, Cyberpunk 2077"),
("PlayStation 5", 500, "2020", "Five Nights at Freddy's: Security Breach, Grand Theft Auto V, Elden Ring, Among Us, Hogwarts Legacy, Cyberpunk 2077"),
("Xbox One", 220, "2013", "Forza Horizon 5, Plants vs. Zombies, Monster Hunter World, Red Dead Redemption 2, Five Nights at Freddy's: Security Breach, Call of Duty: Black Ops III, Grand Theft Auto V, Elden Ring, Rocket League, Among Us, Hogwarts Legacy, Cyberpunk 2077"),
("Xbox Series X/S", 480, "2016", "Forza Horizon 5, Five Nights at Freddy's: Security Breach, Grand Theft Auto V, Elden Ring, Among Us, Hogwarts Legacy, Cyberpunk 2077"),
("Nintendo Switch", 280, "2017", "Skylanders Spyro's Adventure, Plants vs. Zombies, Five Nights at Freddy's: Security Breach, Rocket League, Among Us, Hogwarts Legacy"),
("macOS", 1300, "2001", "Skylanders Spyro's Adventure, Plants vs. Zombies, Call of Duty: Black Ops III, Rocket League"),
("Linux", 750, "1991", "Rocket League"),
("GeForce Now", 100, "2015", "Rocket League"),
("iOS", 760, "2007", "Plants vs. Zombies, Among Us"),
("Android", 260, "2008", "Plants vs. Zombies, Among Us, Hogwarts Legacy"),
("Xbox Cloud Gaming", 15, "2021", "Forza Horizon 5, Among Us"),
("Google Stadia", 130, "2019", "Red Dead Redemption 2, Five Nights at Freddy's: Security Breach, Cyberpunk 2077");




create table Companies(
companieName varchar(255),
companieEmployees int,
creationDate year,
companyGames varchar(255)
);

insert into Companies(companieName, companieEmployees, creationDate, companyGames)
values("Bandai Namco Entertainment", 1115, "2006", "Elden Ring"),
("Psyonix", 238, "2001", "Rocket League"),
("Innersloth", 8, "2015", "Among Us"),
("Warner Bros. Games", 11000, "2004", "Hogwarts Legacy"),
("CD Projekt Red", 859, "2002", "Cyberpunk 2077"),
("Rockstar Games", 5402, "1998", "Grand Theft Auto V, Red Dead Redemption 2"),
("Activision", 13000, "1979", "Call of Duty: Black Ops III, Skylanders Spyro's Adventure"),
("ScottGames", 10, "2014", "Five Nights at Freddy's: Security Breach"),
("Capcom", 3206, "1979", "Monster Hunter World"),
("Electronic Arts", 12900, "1982", "Plants vs. Zombies"),
("PopCap Games", 113, "2000", "Plants vs. Zombies"),
("Playground Games", 402, "2010", "Forza Horizon 5"),
("JP: Square Enix", 5000, "2003", "Skylanders Spyro's Adventure");



create table Players(
playerName varchar(255),
playerAge int,
hoursPlayed int,
creationDate year,
playerGames varchar(255)
);

insert into Players(playerName, playerAge, hoursPlayed, creationDate, playerGames)
values("AsafTheMagniv", 19 , 5000, "2015", "Plants vs. Zombies, Monster Hunter World, Rocket League, Among Us, Grand Theft Auto V, Call of Duty: Black Ops III"),
("CoolDudde69", 22 , 2097, "2009", "Elden Ring, Grand Theft Auto V, Forza Horizon 5, Cyberpunk 2077"),
("Rocket Slayer", 31 , 7379, "2010", "Rocket League, Among Us"),
("Mistake", 25 , 6984, "2016", "Monster Hunter World, Rocket League, Call of Duty: Black Ops III, Plants vs. Zombies"),
("LeSpank", 27 , 5893, "2013", "Forza Horizon 5"),
("SniperGotYou", 23 , 1736, "2018", "Rocket League, Red Dead Redemption 2, Five Nights at Freddy's: Security Breach, Monster Hunter World"),
("MagicKen", 39 , 8134, "2002", "Forza Horizon 5, Plants vs. Zombies, Monster Hunter World, Red Dead Redemption 2, Elden Ring, Rocket League, Hogwarts Legacy, Grand Theft Auto V, Call of Duty: Black Ops III"),
("CrazyMind", 48 , 8255, "2005", "Red Dead Redemption 2, Call of Duty: Black Ops III, Hogwarts Legacy, Elden Ring"),
("BrainAxe", 49 , 11111, "2003", "Call of Duty: Black Ops III, Grand Theft Auto V, Elden Ring, Rocket League, Skylanders Spyro's Adventure"),
("NineTees", 25 , 11063, "2005", "Call of Duty: Black Ops III, Hogwarts Legacy, Forza Horizon 5, Skylanders Spyro's Adventure"),
("Tide2kitchen", 18 , 592, "2021", "Plants vs. Zombies, Elden Ring, Among Us"),
("XboxDesciple", 12 , 4466, "2008", "Red Dead Redemption 2, Cyberpunk 2077, Monster Hunter World, Among Us");







