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
CREATE VIEW matches_per_player AS SELECT players.id AS id, COUNT(*) AS matches FROM players JOIN matches ON players.id = matches.p1 OR players.id = matches.p2 GROUP BY players.id ORDER BY players.id;

CREATE VIEW wins_per_player AS SELECT players.id AS id, COUNT(matches.winner) AS wins FROM players LEFT JOIN matches ON players.id = matches.winner GROUP BY players.id ORDER BY players.id;

-- CREATE VIEW player_standings AS SELECT
