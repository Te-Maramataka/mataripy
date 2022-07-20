from astroquery.jplhorizons import Horizons
from scipy.signal import find_peaks
from timeutils import *


t = arrow.get(datetime(2022,6,26), TIMEZONE)

def findNewMoon(start, stop, step):
    h = Horizons(id='301', location='geocentric', \
                 epochs={'start': arrow2str(start), 'stop': arrow2str(stop), 'step': step})
    v = h.ephemerides(quantities='24')
    idx = find_peaks(v['alpha'])[0]
    return list(map(str2arrow, v['datetime_str'][idx]))
    # return find_peaks(v['alpha'])[0]

def findNewMoonRefine(date, scale='hour'):
    delta = 60
    if scale == 'minute':
        step = '1m'
    else:
        step = '1h'
        delta = delta*24
    return findNewMoon(date.shift(minutes=-delta), date.shift(minutes=delta), step=step)[0]

v = findNewMoon(t.shift(days=-30), t.shift(days=30), '1d')
for s in ['hour', 'minute']:
    v = list(map(lambda x: findNewMoonRefine(x, s), v))

