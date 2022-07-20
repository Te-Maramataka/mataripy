from astroquery.jplhorizons import Horizons
from scipy.signal import find_peaks
from timeutils import *
import itertools


def __findNewMoon(start, stop, step):
    h = Horizons(id='301', location='geocentric', \
                 epochs={'start': arrow2str(start), 'stop': arrow2str(stop), 'step': step})
    v = h.ephemerides(quantities='24')
    idx = find_peaks(v['alpha'])[0]
    l = list(map(str2arrow, v['datetime_str'][idx]))
    return l # if step=='1d' else l[0]
    # return find_peaks(v['alpha'])[0]

def findNewMoon(date, scale='hour'):
    delta = 60
    if scale == 'minute':
        step = '1m'
    elif scale == 'hour':
        step = '1h'
        delta = delta*24
    else:
        step = '1d'
        delta = delta*24*30
    return __findNewMoon(date.shift(minutes=-delta), date.shift(minutes=delta), step=step)


def findNewMoonAround(t):
    v = [t]
    for s in ['day', 'hour', 'minute']:
        v = list(map(lambda x: findNewMoon(x, s), v))
        v = list(itertools.chain(*v))
    return v


if __name__=='__main__':
    t = arrow.get(datetime(2022,6,26), TIMEZONE)
    print(findNewMoonAround(t))
