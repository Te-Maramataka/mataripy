from matariki import *

def displayMatarikiHolidays(years, observers=['500'], displayMonthLength=False):
    divider = '****************************************'
    for obs in observers:
        print()
        print(divider)
        print("Observer location: {}".format("Auckland Observatrory" if obs == '467' else "geocentric"))
        print(divider)
        lineTemplate = "Tangaroa: {} {}, matariki: {}"
        if displayMonthLength:
            lineTemplate += ", Lm: {}"
        for y in years:
            new_moons = getNewMoonAroundMatariki(y, observer=obs)
            t = getMatarikiTangaroa(y, new_moons, observer=obs)
            m = getMatarikiFriday(y, newMoons=new_moons, tangaroa=t, observer=obs)
            lineContent = [t.strftime('%Y %d %b'), t.strftime('%a'), m.strftime('%d %b')]
            if displayMonthLength:
                lineContent.append(getLunarMonthLength(new_moons))
            print(lineTemplate.format(*lineContent))
        print(divider)

if __name__=='__main__':
    displayMatarikiHolidays([2577,2578,2579], displayMonthLength=True)
