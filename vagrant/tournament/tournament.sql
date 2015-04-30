-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;
DROP VIEW IF EXISTS matches_per_player;
DROP VIEW IF EXISTS wins_per_player;
DROP VIEW IF EXISTS player_standings;


CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

/*
DROP TABLE IF EXIST tournaments;
CREATE TABLE tournaments (
);
*/

CREATE TABLE matches (
    p1 INT REFERENCES players (id),
    p2 INT REFERENCES players (id),
    winner INT REFERENCES players (id)
);

-- Views --
CREATE VIEW matches_per_player AS
    SELECT p.id AS id,
        -- The accepted answer at http://stackoverflow.com/questions/28478014/postgresql-left-join-with-bad-count-output
        -- really helped me with the SUM
        --SUM(CASE WHEN p.id = m.p1 OR p.id = m.p2 THEN 1 ELSE 0 END) AS matches
        COUNT(p.id = m.p1 OR p.id = m.p2) AS matches
    FROM players AS p
        LEFT JOIN matches AS m ON p.id IN (m.p1, m.p2)
    GROUP BY p.id
    ORDER BY p.id;

CREATE VIEW wins_per_player AS
    SELECT p.id AS id, COUNT(m.winner) AS wins
    FROM players AS p
        LEFT JOIN matches AS m ON p.id = m.winner
    GROUP BY p.id
    ORDER BY p.id;

-- CREATE VIEW player_standings AS SELECT
CREATE VIEW player_standings AS
    SELECT p.id, p.name, w.wins, m.matches
    FROM players AS p
        JOIN (SELECT * FROM matches_per_player) AS m ON p.id = m.id
        JOIN (SELECT * FROM wins_per_player) AS w ON p.id = w.id
    ORDER BY w.wins DESC;

/* some test-data
 */
INSERT INTO players (name) VALUES('Batman');
INSERT INTO players (name) VALUES('Superman');
INSERT INTO players (name) VALUES('Robin');
INSERT INTO players (name) VALUES('The Hulk');
INSERT INTO players (name) VALUES('Spiderman');

INSERT INTO matches VALUES(1,3,1);
INSERT INTO matches VALUES(1,4,1);
INSERT INTO matches VALUES(4,3,3);
INSERT INTO matches VALUES(3,4,4);
INSERT INTO matches VALUES(2,3,2);
INSERT INTO matches VALUES(2,3,4);
INSERT INTO matches VALUES(1,3,3);
INSERT INTO matches VALUES(1,3,1);
/* some test-data */
