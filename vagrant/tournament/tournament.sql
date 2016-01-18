-- Table definitions for the tournament project.
-- Create the tournament database
CREATE DATABASE tournament;
-- connect to the cournament database
\c tournament

-- create players table
CREATE TABLE players(
    player_id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL
);

-- create matches table
CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner INT REFERENCES players (player_id),
    loser INT REFERENCES players (player_id)
);

-- count regitered players view
CREATE OR REPLACE VIEW count_players AS
    SELECT * FROM players;

-- create the view to select winner from the database
CREATE OR REPLACE VIEW tournament_winner AS
    SELECT matches.winner, players.name, COUNT(*) AS wins
        FROM matches
        LEFT OUTER JOIN players ON matches.winner = plaers.player_id
        GROUP BY winner
        ORDER BY wins DESC;

-- create the view for player standings
CREATE OR REPLACE VIEW current_standings AS
    SELECT  player_id,
            player_name,
            SUM(CASE WHEN players.player_id = matches.winner THEN 1 ELSE 0 END) AS wins,
            COUNT(matches) AS match_count
    FROM players
    LEFT OUTER JOIN matches
    ON players.player_id = matches.winner OR players.player_id = matches.loser
    GROUP BY player_id
    ORDER BY wins DESC,
             match_count ASC;




/* Poulate tables */

-- populate players table
INSERT INTO players (player_name) VALUES ('Bob');
INSERT INTO players (player_name) VALUES ('Tom');
INSERT INTO players (player_name) VALUES ('John');
INSERT INTO players (player_name) VALUES ('Barock');
INSERT INTO players (player_name) VALUES ('James');
INSERT INTO players (player_name) VALUES ('Tammmy');
INSERT INTO players (player_name) VALUES ('Tim');
INSERT INTO players (player_name) VALUES ('Harry');

-- populate matches table
INSERT INTO matches (winner, loser) VALUES (1,2);
INSERT INTO matches (winner, loser) VALUES (3,4);
INSERT INTO matches (winner, loser) VALUES (5,6);
INSERT INTO matches (winner, loser) VALUES (7,8);
