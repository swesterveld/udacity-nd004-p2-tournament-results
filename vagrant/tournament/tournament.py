#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import sys


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname=tournament")
    except:
        sys.exit("Unable to connect to the database")
    return conn


def count_rows_in(table):
    """Count all records in a given table"""
    query = "SELECT COUNT(*) FROM %s;" % table

    conn = connect()
    cur = conn.cursor()

    # Execute a command to query the database and obtain data as Python objects
    cur.execute(query)
    count = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return count


def delete_rows_from(table):
    """Remove all records from a given table in the database."""
    query = "DELETE FROM %s;" % table

    # Connect to the database and open a cursur to perform database operations
    conn = connect()
    cur = conn.cursor()

    # Execute a command to let the database delete the records
    cur.execute(query)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()


def deleteTournaments():
    """Remove all the tournament records from the database."""
    delete_rows_from("tournaments")


def countTournaments():
    """Returns the number of tournaments currently in the database."""
    return count_rows_in("tournaments")


def addTournament(name):
    """Add a tournament to the database."""
    query = "INSERT INTO tournaments (name) VALUES (%s);"
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, (name,))
    cur.close()
    conn.commit()
    conn.close()


def deleteMatches():
    """Remove all the match records from the database."""
    delete_rows_from("matches")


def deletePlayers():
    """Remove all the player records from the database."""
    delete_rows_from("players")


def countPlayers():
    """Returns the number of players currently registered."""
    return count_rows_in("players")


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


def bulkRegisterPlayers(names):
    """Adds multiple players in bulk."""
    for name in names:
        registerPlayer(name)


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
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO matches (p1, p2, winner) VALUES (%s,%s,%s)"

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
    standings = playerStandings()

    next_round = []
    for i in range(0, len(standings), 2):
        next_round.append((standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]))

    return next_round
