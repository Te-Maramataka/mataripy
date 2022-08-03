import arrow

TEAMS = ['EV']
TEAM_PREDITION_DECADE = '/everydecade.txt'
TARGET_PRDITION_DECADE = 'sample_decades.txt'

TEAM_FORMATS = {'EV': 'Do MMMM YYYY'}

def getDatesFromFile(filename, format='YYYY-MM-DD'):
    with open(filename) as f:
        dates = [arrow.get(l.rstrip(), format) for l in f]
    return dates

for team in TEAMS:
    targets = getDatesFromFile(TARGET_PRDITION_DECADE)
    predictions = getDatesFromFile(team + TEAM_PREDITION_DECADE, TEAM_FORMATS[team])
    print(targets[0])
    print(predictions[0])
