#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    conn = psycopg2.connect("dbname=tournament")
    return conn


def deleteMatches():
    """Remove all the match records from the database."""
    query = "DELETE FROM matches;"

    # Connect to the database
    conn = connect()
    # Open a cursur to perform database operations
    cur = conn.cursor()
    # Execute a command
    cur.execute(query)
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    conn.close()



def deletePlayers():
    """Remove all the player records from the database."""
    query = "DELETE FROM players;"

    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    cur.close()
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    query = "SELECT COUNT(*) FROM players;"

    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    # Execute a command to query the database and obtain data as Python
    # objects
    cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    conn.commit()
    conn.close()
    return count



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players (name) VALUES (%s);"

    conn = connect()
    cur = conn.cursor()
    cur.execute(query, (name,))
    cur.close()
    conn.commit()
    conn.close()


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
    query = "SELECT * FROM player_standings;"

    conn = connect()
    cur = conn.cursor()
    cur.execute(query)
    standings = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    print "standings:", standings
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO matches (p1, p2, winner) VALUES (%s)"

    conn = connect()
    cur = conn.cursor()
    cur.execute(query, (winner, loser, winner))
    cur.close()
    conn.commit()
    conn.close()


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


