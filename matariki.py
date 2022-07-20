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

def getMatarikiTangaroa(year):
    new_moons = getNewMoonAroundMatariki(year)
    print("Tangaroa: {},\tLunar Month Length: {}".format(new_moons[0].shift(days=22), getLunarMonthLength(new_moons)))

if __name__=='__main__':
    for y in range(2022,2053):
        getMatarikiTangaroa(y)
