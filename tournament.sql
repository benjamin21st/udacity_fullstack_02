-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Drop database tournament
DROP DATABASE tournament;

-- Create a new database named tournament
CREATE DATABASE tournament;

-- Connect to the database tournament
\c tournament;

-- Create a players table to store players name
CREATE TABLE players (
    player_id serial PRIMARY KEY,
    name text
);

-- Create a matches table to store the winner and loser of each match
CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    winner integer REFERENCES players (player_id),
    loser integer REFERENCES players (player_id)
);

-- standings view
-- Contains the players and their win records, sorted by wins.
CREATE VIEW standings AS
    SELECT
        players.player_id as id, players.name, COALESCE(wins,0) AS wins, COALESCE(matches, 0) AS matches
    FROM
        players

    LEFT JOIN
        (
            SELECT player_id, name, COUNT(player_id) as matches
            FROM players, matches
            WHERE player_id = matches.winner
            OR player_id = matches.loser
            GROUP BY player_id
        ) AS all_matches
    ON
        players.player_id = all_matches.player_id
    LEFT JOIN
        (
            SELECT player_id, name, COUNT(matches.winner) as wins
            FROM players LEFT JOIN matches
            ON player_id = matches.winner
            GROUP BY player_id
        ) AS all_winners
    ON
        all_matches.player_id = all_winners.player_id
    ORDER BY
        wins
    ;


