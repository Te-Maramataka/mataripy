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
* Table Settings: **Sun-Target-Observer ~PHASE angle** (S-T-O) and/or **Sun-Target radial & -vel pos. angle** (PsAng)

When the PsAng increases to 360° (which = 0°), it is a new moon. When it decreases back to 0°, it is a full moon.
For S-T-O, it rises to its a local maximum at new moon, and falls to a local minimum at full moon.
A new moon happens when the S-T-O climbs to a local maximum (should be just below 180°), and full moon when it declines to a local minimum (just above 0°).

Another less accurate method is to look at the PsAng. The PsAng increases to 360° (which = 0°) near a new moon, while decreases to 0° near a full moon. Though the error is usually small, it can be the different between two days in NZST. See the example below.
```
*******************************************************************************
 Date__(UT)__HR:MN        S-T-O    PsAng   PsAMV
************************************************
 2022-May-30 10:30     178.4699  333.229  80.952
 2022-May-30 10:40     178.4841  336.104  80.986
 2022-May-30 10:50     178.4945  339.026  81.021
 2022-May-30 11:00     178.5011  341.981  81.055
 2022-May-30 11:10     178.5037  344.953  81.089  <-- ~ local maximum of S-T-O = new moon
 2022-May-30 11:20     178.5023  347.927  81.124
 2022-May-30 11:30     178.4971  350.888  81.159
 2022-May-30 11:40     178.4879  353.821  81.193
 2022-May-30 11:50     178.4749  356.712  81.228
 2022-May-30 12:00     178.4583  359.548  81.262
 2022-May-30 12:10     178.4380    2.317  81.297
 2022-May-30 12:20     178.4142    5.010  81.332
 2022-May-30 12:30     178.3872    7.619  81.367
 2022-May-30 12:40     178.3570   10.138  81.402
 2022-May-30 12:50     178.3238   12.563  81.436
...
 2022-Jun-14 10:20       2.7703   22.771 273.652
 2022-Jun-14 10:30       2.7476   20.727 273.601
 2022-Jun-14 10:40       2.7283   18.652 273.551
 2022-Jun-14 10:50       2.7124   16.551 273.501
 2022-Jun-14 11:00       2.7001   14.426 273.450
 2022-Jun-14 11:10       2.6913   12.285 273.399
 2022-Jun-14 11:20       2.6861   10.133 273.349
 2022-Jun-14 11:30       2.6846    7.974 273.298  <-- ~ local maximum of S-T-O = full moon
 2022-Jun-14 11:40       2.6868    5.815 273.248
 2022-Jun-14 11:50       2.6925    3.661 273.197
 2022-Jun-14 12:00       2.7019    1.519 273.146
 2022-Jun-14 12:10       2.7148  359.392 273.095
 2022-Jun-14 12:20       2.7313  357.288 273.044
 2022-Jun-14 12:30       2.7512  355.210 272.993
```
In the example above, a new moon occurs at around 2022-May-30 11:10 UTC, but PsAng predicts it to be after 2022-May-30 12:00 UTC, which is a new day, 1 July, in NZST. You may use PsAng to find the rough location of a new moon, and then use S-T-O to get the accurate time.
#### JPL Horizons API Wrappers
* [Python wrapper](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html) - I've written [a python programme](https://github.com/kumkee/solarterms) to predict the 24 Chinese Solar Terms. You may use that as an example.
* [JavaScript wrapper](https://github.com/zachfejes/js-horizons) - I haven't tested this.
* Other languages - you will need to find the wrapper for your langauge, if is other than Python or JavaScript. 
* [Direct API call](https://ssd-api.jpl.nasa.gov/doc/horizons.html) - as an alternative, you can directly call their API
