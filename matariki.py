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
    if t.datetime.day < 19:
        t = t.shift(days=1)
    return t

def getMatarikiFriday(year):
    t = getMatarikiTangaroa(year)
    m = t.shift(days = 4 - t.weekday())
    if m.datetime.day < 19 and m.datetime.month <= 6:
        m = m.shift(days=7)
    return m

if __name__=='__main__':
    for y in range(2022,2053):
        new_moons = getNewMoonAroundMatariki(y)
        t = getMatarikiTangaroa(y, new_moons)
        m = getMatarikiFriday(y)
        print("Tangaroa: {}, {:>9s}, matariki: {}, Lm: {}".format(t, t.strftime('%A'), m, getLunarMonthLength(new_moons)))
        # print("Matariki Holiday: {}".format(m))
