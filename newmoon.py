from astroquery.jplhorizons import Horizons
from scipy.signal import find_peaks

h = Horizons(id='301', location='geocentric', epochs={'start': '2023-Jun-17 00:00', 'stop': '2023-Jul-21 00:00', 'step': '1d'})
v = h.ephemerides(quantities='24')
for i in find_peaks(v['alpha'])[0]:
    print(v[i])

t = arrow.get(datetime(2023,6,19), 'Pacific/Auckland')
