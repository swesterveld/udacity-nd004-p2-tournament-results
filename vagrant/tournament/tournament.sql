-- Table definitions for the tournament project.


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
 *
 * Example:
 *
 *   tournament=> select * from matches_per_player;
 *    id | matches
 *   ----+---------
 *     1 |       4
 *     2 |       3
 *     3 |       6
 *     4 |       4
 *     5 |       3
 *   (5 rows)
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
 *
 * Example:
 *
 *   tournament=> select * from wins_per_player;
 *    id | wins
 *   ----+------
 *     1 |    3
 *     2 |    2
 *     3 |    3
 *     4 |    1
 *     5 |    1
 *   (5 rows)
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
 *
 * Example:
 *
 *   tournament=> select * from player_standings;
 *     id |      name       | wins | matches
 *    ----+-----------------+------+---------
 *      1 | Kiersten Kemper |    3 |       4
 *      3 | Winston Wunsch  |    3 |       6
 *      2 | Elfreda Eakins  |    2 |       3
 *      5 | Katharyn Korth  |    1 |       3
 *      4 | Sudie Sobotka   |    1 |       4
 *    (5 rows)
 */
CREATE VIEW player_standings AS
    SELECT p.id as id, p.name as name, w.wins as wins, m.matches as matches
    FROM players AS p
        JOIN (SELECT * FROM matches_per_player) AS m ON p.id = m.id
        JOIN (SELECT * FROM wins_per_player) AS w ON p.id = w.id
    ORDER BY w.wins DESC, m.matches ASC;
