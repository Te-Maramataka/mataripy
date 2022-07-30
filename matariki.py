from timeutils import *
from newmoon import getNewMoonAround
import functools
import operator


def getNewMoonAroundMatariki(year, observer='geocentric'):
    t = arrow.get(datetime(year, 6, 26), TIMEZONE)
    return getNewMoonAround(t, observer=observer)

def getLunarMonthLength(newMoons):
    time_delta = functools.reduce(operator.sub, map(lambda x: x.floor('day'), newMoons[:2]))
    return -time_delta.days

def getMatarikiTangaroa(year, newMoons=None, observer='geocentric'):
    if not newMoons:
        newMoons = getNewMoonAroundMatariki(year, observer=observer)
    t = newMoons[0].shift(days=22)
    if t.datetime.day < 19:
        t = t.shift(days=1)
    return t.floor('day')

def getMatarikiFriday(year, newMoons=None, tangaroa=None, observer='geocentric'):
    if not newMoons:
        newMoons = getNewMoonAroundMatariki(year, observer=observer)
    if not tangaroa:
        tangaroa = getMatarikiTangaroa(year, newMoons=newMoons, observer=observer)
    m = tangaroa.shift(days = 4 - tangaroa.weekday())
    if m.datetime.day < 19 and m.datetime.month <= 6:
        m = m.shift(days=7)
    return m

if __name__=='__main__':
    pass
