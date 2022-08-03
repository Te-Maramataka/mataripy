import arrow
import numpy as np
from functools import reduce

TEAMS = ['EV', 'Jalja']
TEAM_PREDITION_DECADE = '/everydecade.txt'
TARGET_PRDITION_DECADE = 'sample_decades.txt'

TEAM_FORMATS = {'EV': 'Do MMMM YYYY',
                'Jalja': 'M/D/YYYY'}

def getDatesFromFile(filename, format='YYYY-MM-DD'):
    with open(filename) as f:
        dates = [arrow.get(l.rstrip(), format) for l in f]
    return dates


def calcAccuracy(x, y):
    return sum(x == y) / len(y)


def getYear(d):
    return d.datetime.year


def getYearList(datelist):
    return np.asarray(list(map(getYear, datelist)))


def getAccuracy():
    accuracy = {}
    for team in TEAMS:
        targets = getDatesFromFile(TARGET_PRDITION_DECADE)
        predictions = getDatesFromFile(team + TEAM_PREDITION_DECADE, TEAM_FORMATS[team])
        targets = np.asarray(targets)
        predictions = np.asarray(predictions)
        accuracy[team] = calcAccuracy(predictions, targets), calcAccuracy(getYearList(predictions), getYearList(targets))
    return accuracy

if __name__=='__main__':
    print(getAccuracy())
