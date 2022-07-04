# mataripy
mataripy

## Factors to consider in determining the Matariki holiday
### Friday
It is always a Friday. How to determin the day of the week depends on the language you use. In Javascript, for example, is the [`getDate()` function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay) of the `Date` class. 
### Moon Phase
It is a Tangaroa night. There are normally 4 Tangaroa nights in a Māori lunar month, Tangaroa-ā-mua, Tangaroa-ā-roto, Tangaroa whakapau, and Tangaroa whāriki kiokio. In a 30-night month, these are the 23th to 26th nights. However, Tangaroa are the 23th to 25th nights in a 29-night months. As in Traditional Chinese Calendar, a Māori month starts at new moon.
#### NZST 
We will use midnight in New Zealand Standard Time (UTC+12) to determine the date where the new moon falls. For those trying to use the Traditional Chinese Calendar (TCC), please be mineful that TCC is based on the Chinese Standard Time (UTC+8).
### Apparent position of Matariki cluster to the Sun
The Matariki cluster must be visible at dawn. This turns out to be the easiest factor. Since the Georgian calendar is a solar calendar, we can always predict the Matariki cluster becomes visible at dawn on and after 19 June every year.
If you want to be more precise, it is on and after two days before the June solstice.
### Summary
The Matariki holiday is a Friday during or after the first Tangaroa Luna period after 19 June.
## How to Find Out Moon Phase
### Recommended Way - JPL Horizons
The most accurate way to calculate the moon phase is through [Horizon System](https://ssd.jpl.nasa.gov/horizons/) from NASA's Jet Propulsion Laboratory. For a quick check, you can use their [web app](https://ssd.jpl.nasa.gov/horizons/app.html). However, to do arbitary prediction, you will need to use their [API](https://ssd-api.jpl.nasa.gov/doc/horizons.html) or a third party API wrapper for your language. More on that later.
#### Moon Phase from JPL Horizons
To predict the moon phase, you may use the following setting:
* Ephemeris Type: Observer Table
* Target body: **Moon**
* Observer Location: **Geocentric**
* Table Settings: **Sun-Target radial & -vel pos. angle** (PsAng) and/or **Sun-Target-Observer ~PHASE angle** (S-T-O)

When the PsAng increases to 360° (which = 0°), it is a new moon. When it decreases back to 0°, it is a full moon.
For S-T-O, it rises to its a local maximum at new moon, and falls to a local minimum at full moon.
