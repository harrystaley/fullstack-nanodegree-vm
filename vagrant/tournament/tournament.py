'''This houses the python functions used to work the database.'''
# !/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def delete_matches():
    """Remove all the match records from the database."""
    c = connect.cursor()
    c.execute("DELETE FROM matches")
    connect.commit()
    connect.close()

def delete_players():
    """Remove all the player records from the database."""
    c = connect.cursor()
    c.execute("DELETE FROM players")
    connect.commit()
    connect.close()


def count_players():
    """Returns the number of players currently registered."""
    c = connect.cursor()
    c.execute("SELECT * FROM count_players")
    connect.commit()
    player_count = c.fetchall()
    connect.close()
    return player_count


def is_even(i):
    """ Returns a boolean falue telling if the value is even """
    return (i % 2) == 0


def register_player(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
      WARNING: some names may be modified in order to protect the database.
    """

    """ use bleach to clean the name of the registered user """
    clean_name = bleach.clean(name, strip=True)

    c = connect.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (clean_name))
    connect.commit()
    connect.close()


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        player_id: the player's unique id (assigned by the database)
        player_name: the player's full name (as registered)
        wins: the number of matches the player has won
        match_count: the number of matches the player has played
    """
    c = connect.cursor()
    c.execute("SELECT * FROM current_standings")
    connect.commit()
    connect.close()


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    c = connect.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s);", (winner, loser))
    connect.commit()
    connect.close()

def swiss_pairings():
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

    """ Get player_count from count_players function """
    player_count = count_players()
    """ determine if playercount is an even number """
    if is_even(player_count) == True:
        match_pairings = player_count / 2

        """ Pair players into matches. """
        for x in xrange(match_pairings):


    else: raise ValueError("The tournament requires and even number of players. \
                            Please add or remove a single player.")

    c = connect.cursor()

    connect.commit()
    connect.close()


