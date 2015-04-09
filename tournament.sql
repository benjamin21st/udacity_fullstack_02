-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE IF NOT EXISTS players (
    id serial PRIMARY KEY,
    name varchar(40) NOT NULL,
    num_of_wins integer NOT NULL DEFAULT 0,
    matches integer NOT NULL DEFAULT 0
);


CREATE TABLE IF NOT EXISTS matches (
    id serial PRIMARY KEY,
    player1 int NOT NULL,
    player2 int
);

