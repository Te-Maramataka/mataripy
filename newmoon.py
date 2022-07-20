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

v = [arrow.get(datetime(2022,6,26), TIMEZONE)]

for s in ['day', 'hour', 'minute']:
    v = list(map(lambda x: findNewMoon(x, s), v))
    v = list(itertools.chain(*v))
# v = findNewMoonRefine(v, 'day')
# v = findNewMoonRefine(v.shift(days=-30), v.shift(days=30), '1d')
#for s in ['hour', 'minute']:
#    v = list(map(lambda x: findNewMoonRefine(x, s), v))

#for s in ['day', 'hour', 'minute']:
#    v = list(map(lambda x: findNewMoonRefine(x, s), v))

# v = list(map(lambda x: findNewMoonRefine(x, 'day'), v))
