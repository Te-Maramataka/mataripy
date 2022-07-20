from timeutils import *
from newmoon import getNewMoonAround


def getNewMoonAroundMatariki(y):
    t = arrow.get(datetime(y, 6, 26), TIMEZONE)
    return getNewMoonAround(t)


if __name__=='__main__':
    print(getNewMoonAroundMatariki(2028))
