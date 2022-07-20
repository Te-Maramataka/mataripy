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

if __name__=='__main__':
    print(getNewMoonAroundMatariki(2028))
