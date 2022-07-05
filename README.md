# Factors to consider in determining the Matariki holiday
## Friday
It is always a Friday. How to determin the day of the week depends on the language you use. In Javascript, for example, is the [`getDate()` function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay) of the `Date` class. 
## Moon Phase
It is a Tangaroa night. There are normally 4 Tangaroa nights in a Māori lunar month, Tangaroa-ā-mua, Tangaroa-ā-roto, Tangaroa whakapau, and Tangaroa whāriki kiokio. In a 30-night month, these are the 23th to 26th nights. However, Tangaroa are the 23th to 25th nights in a 29-night months. As in Traditional Chinese Calendar, a Māori month starts at new moon.
## NZST 
We will use midnight in New Zealand Standard Time (UTC+12) to determine the date where the new moon falls. For those trying to use the Traditional Chinese Calendar (TCC), please be mineful that TCC is based on the Chinese Standard Time (UTC+8).
## Apparent position of Matariki cluster to the Sun
The Matariki cluster must be visible at dawn. This turns out to be the easiest factor. Since the Georgian calendar is a solar calendar, we can always predict the Matariki cluster becomes visible at dawn on and after 19 June every year.
If you want to be more precise, it is on and after two days before the June solstice.
## Summary
The Matariki holiday is a Friday during or after the first Tangaroa Luna period after 19 June.
# How to Find Out Moon Phase
## Recommended Way - JPL Horizons
The most accurate way to calculate the moon phase is through [Horizon System](https://ssd.jpl.nasa.gov/horizons/) from NASA's Jet Propulsion Laboratory. For a quick check, you can use their [web app](https://ssd.jpl.nasa.gov/horizons/app.html). However, to do arbitary prediction, you will need to use their [API](https://ssd-api.jpl.nasa.gov/doc/horizons.html) or a third party API wrapper for your language. More on that later.
## Moon Phase from JPL Horizons
To predict the moon phase, you may use the following setting:
* Ephemeris Type: Observer Table
* Target body: **Moon**
* Observer Location: **Geocentric**
* Table Settings: **Sun-Target-Observer ~PHASE angle** (S-T-O) 

There is a [Wikipedia page about the S-T-O phase angle](https://en.wikipedia.org/wiki/Phase_angle_%28astronomy%29). 

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Phase_Angle_3.svg/1280px-Phase_Angle_3.svg.png" alt="S-T-O" width="300"/>

A new moon happens when the S-T-O climbs to a local maximum (should be just below 180°), and full moon when it declines to a local minimum (just above 0°).
```
*******************************************************************************
 Date__(UT)__HR:MN        S-T-O    PsAng   PsAMV
************************************************
 2022-May-30 11:06     178.5031
 2022-May-30 11:07     178.5033
 2022-May-30 11:08     178.5035
 2022-May-30 11:09     178.5036
 2022-May-30 11:10     178.5037
 2022-May-30 11:11     178.5037 <-- local maximum = new moon
 2022-May-30 11:12     178.5037
 2022-May-30 11:13     178.5037
 2022-May-30 11:14     178.5036
 2022-May-30 11:15     178.5035
 2022-May-30 11:16     178.5033
 2022-May-30 11:17     178.5031
...
 2022-Jun-14 11:24       2.6851
 2022-Jun-14 11:25       2.6849
 2022-Jun-14 11:26       2.6848
 2022-Jun-14 11:27       2.6847
 2022-Jun-14 11:28       2.6846
 2022-Jun-14 11:29       2.6846  <-- local minimum = full moon
 2022-Jun-14 11:30       2.6846
 2022-Jun-14 11:31       2.6847
 2022-Jun-14 11:32       2.6848
 2022-Jun-14 11:33       2.6849
 2022-Jun-14 11:34       2.6850
```
In the example above, a new moon occurs at around 2022-May-30 11:11 UTC, and a full moon at around 2022-Jun-14 11:29.
## JPL Horizons API Wrappers
* [Python wrapper](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html) - I've written [a python programme](https://github.com/kumkee/solarterms) to predict the 24 Chinese Solar Terms. You may use that as an example.
* [JavaScript wrapper](https://github.com/zachfejes/js-horizons) - I haven't tested this.
* Other languages - you will need to find the wrapper for your langauge, if is other than Python or JavaScript. 
* [Direct API call](https://ssd-api.jpl.nasa.gov/doc/horizons.html) - as an alternative, you can directly call their API
