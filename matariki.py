from timeutils import *
from newmoon import getNewMoonAround
import functools
import operator


def getNewMoonAroundMatariki(year):
    t = arrow.get(datetime(year, 6, 26), TIMEZONE)
    return getNewMoonAround(t)

def getLunarMonthLength(newMoons):
    time_delta = functools.reduce(operator.sub, map(lambda x: x.floor('day'), newMoons[:2]))
    return -time_delta.days

def getMatarikiTangaroa(year, newMoons = None):
    if not newMoons:
        newMoons = getNewMoonAroundMatariki(year)
    t = newMoons[0].shift(days=22)
    if t.datetime.day <19:
        t.shift(days=1)
    return t

if __name__=='__main__':
    for y in range(2022,2053):
        new_moons = getNewMoonAroundMatariki(y)
        t = getMatarikiTangaroa(y, new_moons)
        print("Tangaroa: {},\t{:>9s},\tLunar Month Length: {}".format(t, t.strftime('%A'), getLunarMonthLength(new_moons)))
