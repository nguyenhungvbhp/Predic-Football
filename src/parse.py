#!/usr/bin/env python

"""
    This script can parse CSV databases.

    To use it, you should call getInfo(teamName) function.
    It returns the list with following structure:
        [TeamName, OpponentTeamName, TeamNameScore, OpponentTeamNameScore, 
         TeamNameSignificance, OpponentTeamNameSignificanceisTeamNameHome].
    If team played the match at the home stadium, isTeamHome returns True, otherwise - False.
"""

import os
import csv

dir = "/Users/manhhung/Documents/BKHN/ML/workspace/pre_football/football-results-prediction-ml/datasets"
dirTrain = "/Users/manhhung/Documents/BKHN/ML/workspace/pre_football/football-results-prediction-ml/data_train"
txtDir = "/Users/manhhung/Documents/BKHN/ML/workspace/pre_football/football-results-prediction-ml/txt"
teamName = ""
teams = []
teamSignificance = ""
opponentTeamSignificance = ""
teamsStat = []
matchesNumber = 1000


def getTeamsNamesList():
    teamsFile = open(dir + "/allTeams.txt", 'r')
    for team in teamsFile:
        teams.append(team.split(","))
    teamsFile.close();


def getInfo(teams, matchesNumber):
    for team in teams:
        if team[1].endswith("\n"):
            team[1] = team[1][:team[1].find("\n")]
        teamName = team[0]
        teamSignificance = team[1]
        getCSV(teamName, teamSignificance, matchesNumber)
        del teamsStat[:]


def getCSV(teamName, teamSignificance, matchesNumber):
    for name in os.listdir(dir):
        # print(name)
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            if name.endswith("csv"):
                print(name)
                # print(teamName)
                # parseCSV(path, teamName, teamSignificance, matchesNumber)
        else:
            getCSV(dir)
        saveResults(teamsStat, teamName)


def parseCSV(path, teamName, teamSignificance, matchesNumber):
    inputFile = open(path, "rb")
    rdr = csv.reader(inputFile)
    for rec in rdr:
        try:
            # print(rec)
            if (len(teamsStat) <= matchesNumber):
                isTeamHome = rec[2] == teamName
                isTeamAway = rec[3] == teamName
                for team in teams:
                    if isTeamHome:
                        if (team[0] == rec[3]):
                            opponentTeamSignificance = team[1]
                    if isTeamAway:
                        if (team[0] == rec[2]):
                            opponentTeamSignificance = team[1]
                if opponentTeamSignificance.endswith("\n"):
                    opponentTeamSignificance = opponentTeamSignificance[
                                               :opponentTeamSignificance.find("\n")]
                if isTeamHome:
                    teamsStat.append([rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9], rec[10], rec[12],
                                      rec[13], rec[14], rec[15], rec[16], rec[17], rec[18], rec[19], rec[20], rec[21],
                                      rec[22], rec[23], teamSignificance, opponentTeamSignificance, str(isTeamHome)])
                elif isTeamAway:
                    teamsStat.append([rec[3], rec[2], rec[5], rec[4],
                                      rec[6], rec[7], rec[8], rec[9], rec[10], rec[12],
                                      rec[13], rec[14], rec[15], rec[16], rec[17], rec[18], rec[19], rec[20], rec[21],
                                      rec[22], rec[23],
                                      teamSignificance, opponentTeamSignificance, str(isTeamHome)])
        except:
            pass
    inputFile.close()


def saveResults(teamsStat, teamName):
    resFile = open(txtDir + "/sortedData" + teamName.replace(" ", "_") + ".txt", 'w')
    for stat in teamsStat:
        resFile.write(';'.join(stat) + '\n')
    resFile.close()


def fn():  # 1.Get file names from directory
    file_list = os.listdir(dir)
    listCSV = []
    for name in file_list:
        if name.endswith('csv'):
            listCSV.append(name)
    return listCSV


dicsNameTeam = {
    "Arsenal": 3,
    "Aston Villa": 7,
    "Birmingham": 8,
    "Blackburn": 9,
    "Blackpool": 10,
    "Bolton": 11,
    "Bournemouth": 12,
    "Burnley": 13,
    "Cardiff": 14,
    "Charlton": 15,
    "Chelsea": 2,
    "Crystal Palace": 16,
    "Derby": 17,
    "Everton": 7,
    "Fulham": 18,
    "Hull": 19,
    "Leeds": 20,
    "Leicester": 21,
    "Liverpool": 4,
    "Man City": 6,
    "Man United": 1,
    "Middlesbrough": 22,
    "Newcastle": 23,
    "Norwich": 24,
    "Portsmouth": 25,
    "QPR": 26,
    "Reading": 27,
    "Sheffield United": 28,
    "Southampton": 29,
    "Stoke": 30,
    "Sunderland": 31,
    "Swansea": 32,
    "Tottenham": 5,
    "Watford": 33,
    "West Brom": 34,
    "West Ham": 35,
    "Wigan": 36,
    "Wolves": 37,
    "Brighton": 38,
    "Huddersfield": 39}


def parseCSV(path):
    f = open(path, 'rb')
    reader = csv.reader(f)
    reader = list(reader)
    reader = reader[1:]
    f.close()

    listHome = []
    listAway = []
    dataTrain = []
    for i in range(len(reader)):
        currentMatch = reader[i]
        listLastMatch = reader[0: i]

        for lastMatch in listLastMatch:
            if currentMatch[2] in lastMatch:
                listHome.append(lastMatch)
            if currentMatch[3] in lastMatch:
                listAway.append(lastMatch)

        gdHome = 0
        gdAway = 0
        HS = 0
        AS = 0
        HST = 0
        AST = 0
        HC = 0
        AC = 0
        HF = 0
        AF = 0
        HY = 0
        AY = 0
        HR = 0
        AR = 0
        scoreHome = 0
        scoreAway = 0
        for j in range(len(listHome)):
            lostGoalHome = 0
            winGoalHome = 0
            HS = 0
            # Neu doi 1 la doi chu nha trong lich su cua no
            if listHome[j][2] == currentMatch[2]:
                winGoalHome = int(listHome[j][4])
                lostGoalHome = int(listHome[j][5])
                if listHome[j][6] == "H":
                    scoreHome += 3
                elif listHome[j][6] == "D":
                    scoreHome += 1
            else:
                winGoalHome = int(listHome[j][5])
                lostGoalHome = int(listHome[j][4])
                if listHome[j][6] == "A":
                    scoreHome += 3
                elif listHome[j][6] == "D":
                    scoreHome += 1
            gdHome += (winGoalHome - lostGoalHome)
        # home
        if len(listHome) > 5:
            for m in range(len(listHome) - 1, len(listHome) - 6, -1):
                if listHome[m][2] == currentMatch[2]:
                    HS += int(listHome[m][11])
                    HST += int(listHome[m][13])
                    HF += int(listHome[m][15])
                    HC += int(listHome[m][17])
                    HY += int(listHome[m][19])
                    HR += int(listHome[m][21])
                else:
                    HS += int(listHome[m][12])
                    HST += int(listHome[m][14])
                    HF += int(listHome[m][16])
                    HC += int(listHome[m][18])
                    HY += int(listHome[m][20])
                    HR += int(listHome[m][22])
        elif (len(listHome) <= 5) and (len(listHome) > 0):
            for m in range(len(listHome)):
                if listHome[m][2] == currentMatch[2]:
                    HS += int(listHome[m][11])
                    HST += int(listHome[m][13])
                    HF += int(listHome[m][15])
                    HC += int(listHome[m][17])
                    HY += int(listHome[m][19])
                    HR += int(listHome[m][21])
                else:
                    HS += int(listHome[m][12])
                    HST += int(listHome[m][14])
                    HF += int(listHome[m][16])
                    HC += int(listHome[m][18])
                    HY += int(listHome[m][20])
                    HR += int(listHome[m][22])

        # Away
        if len(listAway) > 5:
            for m in range(len(listAway) - 1, len(listAway) - 6, -1):
                if listAway[m][2] == currentMatch[3]:
                    AS += int(listAway[m][11])
                    AST += int(listAway[m][13])
                    AF += int(listAway[m][15])
                    AC += int(listAway[m][17])
                    AY += int(listAway[m][19])
                    AR += int(listAway[m][21])
                else:
                    AS += int(listAway[m][12])
                    AST += int(listAway[m][14])
                    AF += int(listAway[m][16])
                    AC += int(listAway[m][18])
                    AY += int(listAway[m][20])
                    AR += int(listAway[m][22])
        elif (len(listAway) <= 5) and (len(listAway) > 0):
            for m in range(len(listAway)):
                if listAway[m][2] == currentMatch[3]:
                    AS += int(listAway[m][11])
                    AST += int(listAway[m][13])
                    AF += int(listAway[m][15])
                    AC += int(listAway[m][17])
                    AY += int(listAway[m][19])
                    AR += int(listAway[m][21])
                else:
                    AS += int(listAway[m][12])
                    AST += int(listAway[m][14])
                    AF += int(listAway[m][16])
                    AC += int(listAway[m][18])
                    AY += int(listAway[m][20])
                    AR += int(listAway[m][22])

        for j in range(len(listAway)):
            lostGoalAway = 0
            winGoalAway = 0
            # Neu doi thu 2 la doi chu nha trong cac tran dau truoc cua no
            if listAway[j][2] == currentMatch[3]:
                winGoalAway = int(listAway[j][4])
                lostGoalAway = int(listAway[j][5])
                if listAway[j][6] == "H":
                    scoreAway += 3
                elif listAway[j][6] == "D":
                    scoreAway += 1
            else:
                winGoalAway = int(listAway[j][5])
                lostGoalAway = int(listAway[j][4])
                if listAway[j][6] == "A":
                    scoreAway += 3
                elif listAway[j][6] == "D":
                    scoreAway += 1

            gdAway += (winGoalAway - lostGoalAway)
        # print(str(i + 1) + ": " + str(dicsNameTeam[currentMatch[2]]) + " vs " + str(
        #     dicsNameTeam[currentMatch[2]]) + "|GD Home: " + str(gdHome) +
        #       "|GD Away: " + str(gdAway) + " |HS: " + str(HS) + " |AS: " + str(AS) + \
        #       "|HST: " + str(HST) + " |AST: " + str(AST) + " |HF: " + str(HF) + " |AF: " + \
        #       str(AF) + " |HC: " + str(HC) + " |AC: " + str(AC) + \
        #       " |HY: " + str(HY) + " |AY: " + str(AY) + " |HR: " + str(HR) + " |AR: " + str(AR) + \
        #       "| Score Home: " + str(scoreHome) + " |Score away: " + str(scoreAway) + "| Outcome: " + currentMatch[9])
        result = 0
        if (currentMatch[9] == "H"):
            result = 1
        elif (currentMatch[9] == "A"):
            result = -1

        dataTrain.append(
            [str(dicsNameTeam[currentMatch[2]]), str(dicsNameTeam[currentMatch[3]]),currentMatch[23], currentMatch[24], currentMatch[25], currentMatch[26], currentMatch[27], currentMatch[28], str(gdHome), str(gdAway), str(scoreHome), str(scoreAway), result])

        listHome = []
        listAway = []
    print(path)
    myFile = open(dirTrain + "/datatrain1.csv", 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(dataTrain)


# def writeFile():
#     # myData = [["first_name", "second_name", "Grade"],
#     #       ['Alex', 'Brian', 'A'],
#     #       ['Tom', 'Smith', 'B']]
#
#     myData = [
#         ["idHome", "idAway", "GD Home", "GD Away", "HS", "AS", "HST", "AST", "HF", "AF",
#          "HC", "AC", "HY", "AY", "HR", "AR", "Point Home", "Point Away", "Outcome"]]
#     myFile = open(dirTrain + "/datatrain.csv", 'a')
#     with myFile:
#         writer = csv.writer(myFile)
#         writer.writerows(myData)


def writeDataTrain():
    listFile = fn()
    for file in listFile:
        path = dir + "/" + str(file)
        parseCSV(path)
        # print(file)


if __name__ == '__main__':
    # getTeamsNamesList()
    # getInfo(teams, matchesNumber)
    # parseCSV(dir + "/E01415.csv")
    writeDataTrain()
