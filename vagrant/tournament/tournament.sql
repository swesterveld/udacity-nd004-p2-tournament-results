-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

DROP TABLE IF EXISTS players;
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

/*
DROP TABLE IF EXIST tournaments;
CREATE TABLE tournaments (
);
*/

DROP TABLE IF EXISTS matches;
CREATE TABLE matches (
    p1 INT REFERENCES players (id),
    p2 INT REFERENCES players (id),
    winner INT REFERENCES players (id)
);
