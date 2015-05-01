#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteTournaments():
    deleteTournaments()
    print "0. Tournaments can be deleted."


def testAddCountDeleteTournaments():
    deleteTournaments()
    addTournament("Tournament A")
    addTournament("Tournament B")
    c = countTournaments()
    if c != 2:
        raise ValueError(
            "After 2 tournaments added, countTournaments() should return 2.")
    deleteTournaments()
    c = countTournaments()
    if c == '0':
        raise TypeError(
            "countTournaments() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError(
            "After deleting, countTournaments() should return 0.")
    print "0.5 Tournaments can be added and deleted."


def testDeleteMatches():
    deleteTournaments()
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers() should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    players = ["Markov Chaney", "Joe Malik", "Mao Tsu-hsi", "Atlanta Hope"]
    bulkRegisterPlayers(players)
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    players = ["Melpomene Murray", "Randy Schwartz"]
    bulkRegisterPlayers(players)
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testStandingsOrdering():
    """Test ordering of player standings, according to OMW (Opponent Match
    Wins) when multiple players have the smae number of wins."""
    deleteMatches()
    deletePlayers()
    players = ["Kiersten Kemper", "Elfreda Eakins", "Winston Wunsch",
               "Sudie Sobotka", "Katharyn Korth"]
    bulkRegisterPlayers(players)
    standings = playerStandings()
    [id1, id2, id3, id4, id5] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id2, id3)
    reportMatch(id3, id4)
    reportMatch(id4, id5)
    reportMatch(id5, id1)
    reportMatch(id1, id3)
    reportMatch(id1, id3)
    reportMatch(id2, id4)
    reportMatch(id3, id5)
    reportMatch(id3, id4)
    standings = playerStandings()
    names = [row[1] for row in standings]
    players = ["Kiersten Kemper", "Winston Wunsch", "Elfreda Eakins",
               "Katharyn Korth", "Sudie Sobotka"]
    if names != players:
        raise ValueError("Ordering of standings should be according to OMW.")
    print "6.5 Players appear in standings according to OMW."


def testReportMatches():
    deleteMatches()
    deletePlayers()
    players = ["Bruno Walton", "Boots O'Neal", "Cathy Burton", "Diane Grant"]
    bulkRegisterPlayers(players)
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deletePlayers()
    players = ["Twilight Sparkle", "Fluttershy", "Applejack", "Pinkie Pie"]
    bulkRegisterPlayers(players)
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    testDeleteTournaments()
    testAddCountDeleteTournaments()
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testStandingsOrdering()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"


