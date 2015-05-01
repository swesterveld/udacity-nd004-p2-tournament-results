-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


/* Commented out
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
*/

DROP TABLE IF EXISTS tournaments CASCADE;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS matches CASCADE;
DROP VIEW IF EXISTS matches_per_player;
DROP VIEW IF EXISTS wins_per_player;
DROP VIEW IF EXISTS player_standings;


/* 
 * This table will be needed to support more than one tournament.
 * TODO: fully support/implement tournaments in the code.
 */
CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

/*
 * This table will be needed to support more than one tournament.
 * TODO: fully support/implement enrollments in the code.
 */
CREATE TABLE enrollments (
    player INT REFERENCES players (id),
    tournament INT REFERENCES tournaments (id)
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    tournament INT REFERENCES tournaments (id),
    p1 INT REFERENCES players (id),
    p2 INT REFERENCES players (id),
    winner INT REFERENCES players (id)
);


-- Views --

/*
 * Get overview of the number of matches each player has played.
 * Each row has the players' id and (total) number of matches.
 */
CREATE VIEW matches_per_player AS
    SELECT p.id AS id,
        COUNT(p.id = m.p1 OR p.id = m.p2) AS matches
    FROM players AS p
        LEFT JOIN matches AS m ON p.id IN (m.p1, m.p2)
    GROUP BY p.id
    ORDER BY p.id;

/*
 * Get overview of the number of wins for each player.
 * Each row has the players' id, and (total) number of wins.
 */
CREATE VIEW wins_per_player AS
    SELECT p.id AS id, COUNT(m.winner) AS wins
    FROM players AS p
        LEFT JOIN matches AS m ON p.id = m.winner
    GROUP BY p.id
    ORDER BY p.id;

/*
 * Get player standings, ranked according to OMW (Opponent Match Wins).
 * Each row has the players' id, name, #wins and #matches.
 */
CREATE VIEW player_standings AS
    SELECT p.id as id, p.name as name, w.wins as wins, m.matches as matches
    FROM players AS p
        JOIN (SELECT * FROM matches_per_player) AS m ON p.id = m.id
        JOIN (SELECT * FROM wins_per_player) AS w ON p.id = w.id
    ORDER BY w.wins DESC, m.matches ASC;
