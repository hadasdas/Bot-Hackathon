USE sql_intro;

-- CREATE TABLE moods(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     mood_type VARCHAR(20)
-- );

-- CREATE TABLE bot_users(
--     id BIGINT NOT NULL PRIMARY KEY,
--     state INT,
--     mood INT,

--     FOREIGN KEY(mood) REFERENCES moods(id)
-- );

-- INSERT INTO moods VALUES(null, 'happy');
-- INSERT INTO moods VALUES(null, 'excited');
-- INSERT INTO moods VALUES(null, 'ok');
-- INSERT INTO moods VALUES(null, 'sad');
-- INSERT INTO moods VALUES(null, 'stressed out');

-- SELECT * FROM bot_users;

-- CREATE TABLE category
-- (
--     id INT NOT NULL PRIMARY KEY,
--     name_category VARCHAR(30)
-- )

-- CREATE TABLE music(
--     name_music VARCHAR(200),
--     url_music VARCHAR(200),
--     id INT NOT NULL ,
--     artist VARCHAR(40),
--     year_publication INT,
--     FOREIGN KEY(id) REFERENCES category(id),
--     PRIMARY KEY(url_music)
-- )

-- INSERT INTO category VALUES(0, "Party");
-- INSERT INTO category VALUES(1, "Mellow");
-- INSERT INTO category VALUES(2, "Energizing_pop");
-- INSERT INTO category VALUES(3, "Hebrew_fun");
-- INSERT INTO category VALUES(4, "Hebrew_mellow");
-- INSERT INTO category VALUES(5, "Chasidic");
-- INSERT INTO category VALUES(6, "Meditation");

-- INSERT INTO music VALUES("Party Mix 2019", "https://www.youtube.com/watch?v=uFAWIKVThjA",
-- 0,"Mashup Mixes",2019);
-- INSERT INTO music VALUES("PARTY MIX 2020|Quarantine & Lockdown Mix|COVID-19", "https://www.youtube.com/watch?v=7EBxB5sqhoA&list=RDuFAWIKVThjA&index=2",
-- 0,"Valentino Sirolli",2020);
-- INSERT INTO music VALUES("IBIZA SUMMER MIX 2020 ", "https://www.youtube.com/watch?v=0IA1vCyffos",
-- 0,"Queen Deep",2020);
-- INSERT INTO music VALUES("Festival Music Mix 2016", "https://www.youtube.com/watch?v=MKXK8xwYDIA",
-- 0,"ElectroDanceMixes",2016);
-- INSERT INTO music VALUES("EDM Mashup Mix 2020 - Best Mashups & Remixes", "https://www.youtube.com/watch?v=nMH6AvpHXb8",
-- 0,"TYSON Music",2020);

-- SELECT * FROM music
-- WHERE id=0;


-- insert music with mellow category
-- INSERT INTO music VALUES("Mellow Rock Your All time Favorite 2020", "https://www.youtube.com/watch?v=kgMVF1iSDzM",
-- 1,"Slow Rock BM",2020);
-- INSERT INTO music VALUES("Ed Sheeran - Perfect", "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PL7W9LuUf6bFrvd4NVz2iGQg1AP46za4Ra",
-- 1,"Ed Sheeran",2017);
-- INSERT INTO music VALUES("Calum Scott - You Are The Reason", "https://www.youtube.com/watch?v=ShZ978fBl6Y",
-- 1,"Calum Scott",2018);
-- INSERT INTO music VALUES("James Arthur - Say You Won't Let Go", "https://www.youtube.com/watch?v=0yW7w8F2TVA",
-- 1,"James Arthur",2016);
-- INSERT INTO music VALUES("Ky Baldwin - Dear Mom (Official Music Video) ft. Mindy Pack", "https://www.youtube.com/watch?v=AM_hKCMXJ0o",
-- 1,"Ky Baldwin",2019);

-- -- SELECT * FROM music;
-- -- WHERE id=1


-- -- insert music with Energizing_pop category
-- INSERT INTO music VALUES("Ed Sheeran - Shape of You", "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj",
-- 2,"Ed Sheeran",2017);
-- INSERT INTO music VALUES("OneRepublic - Counting Stars", "https://www.youtube.com/watch?v=hT_nvWreIhg",
-- 2,"OneRepublic",2013);
-- INSERT INTO music VALUES("The Jackson 5 - I Want You Back", "https://www.youtube.com/watch?v=s3Q80mk7bxE",
--  2, "The Jackson 5", 1971);
-- INSERT INTO music VALUES("Beyonce - Single ladies", "https://www.youtube.com/watch?v=0wsTogFALXg",
--  2, "Beyonce", 2009)
-- INSERT INTO music VALUES("Ha'Dorbanim - Yatzanu Lirkod", "https://www.youtube.com/watch?v=c2et21ilxko",
-- 2, "Ha'Dorbanim", 2003)
-- INSERT INTO music VALUES("Village People - YMCA", "https://www.youtube.com/watch?v=CS9OO0S5w2k",
-- 2, "Village People", 1978)
-- INSERT INTO music VALUES("Kool & The Gang - Celebration", "https://www.youtube.com/watch?v=3GwjfUFyY6M",
-- 2, "Kool & The Gang", 1980)