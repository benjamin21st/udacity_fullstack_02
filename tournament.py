#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def execute_query(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    return c


def deleteMatches():
    """Remove all the match records from the database."""
    execute_query("UPDATE players SET matches = 0")


def deletePlayers():
    """Remove all the player records from the database."""
    execute_query("DELETE FROM players")


def countPlayers():
    """Returns the number of players currently registered."""
    result = execute_query("SELECT COUNT(*) FROM players").fetchone()[0]
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # The first query of this one is a bit tricky, I couldn't seem to integrate
    # the tuple c.execute(query, value) to my execute_query function
    # so I used this lengthy way as a work around
    conn = connect()
    c = conn.cursor()
    query = "INSERT INTO players (name) values (%s)"
    c.execute(query, (name,))
    conn.commit()
    c.execute("SELECT COUNT(*) FROM players")
    return c.fetchone()[0]


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    results = execute_query("SELECT * FROM players ORDER BY num_of_wins DESC")
    return results.fetchall()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query_winner = "UPDATE players SET num_of_wins = num_of_wins + 1, matches = matches + 1 WHERE id = %d" % winner
    query_loser = "UPDATE players SET matches = matches + 1 WHERE id = %d" % loser

    execute_query(query_winner)
    execute_query(query_loser)

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    players = execute_query("SELECT * FROM players ORDER BY num_of_wins DESC").fetchall()
    results = []

    for i in xrange(0, len(players) - 1, 2):
        pair = (players[i][0], players[i][1], players[i+1][0], players[i+1][1])
        results.append(pair)
        print results

    return results




