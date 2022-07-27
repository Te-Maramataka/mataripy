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

def getMatarikiTangaroa(year, newMoons = None, observer='geocentric'):
    if not newMoons:
        newMoons = getNewMoonAroundMatariki(year, observer=observer)
    t = newMoons[0].shift(days=22)
    if t.datetime.day < 19:
        t = t.shift(days=1)
    return t.floor('day')

def getMatarikiFriday(year, observer='geocentric'):
    t = getMatarikiTangaroa(year, observer=observer)
    m = t.shift(days = 4 - t.weekday())
    if m.datetime.day < 19 and m.datetime.month <= 6:
        m = m.shift(days=7)
    return m

if __name__=='__main__':
    obs = '467'# 'geocentric'
    for y in range(2022,2053):
        new_moons = getNewMoonAroundMatariki(y, observer=obs)
        t = getMatarikiTangaroa(y, new_moons, observer=obs)
        m = getMatarikiFriday(y, observer=obs)
        print("Tangaroa: {}, {}, matariki: {}, Lm: {}"
              .format(t.strftime('%Y %d %b'), t.strftime('%a'), m.strftime('%d %b'), getLunarMonthLength(new_moons)))
