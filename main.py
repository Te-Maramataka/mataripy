from matariki import *

def displayMatarikiHolidays(years, observers=['500'], displayMonthLenght=False):
    for obs in observers:
        print()
        print('****************************************')
        print("Observer location: {}".format("Auckland Observatrory" if obs == '467' else "geocentric"))
        print('****************************************')
        lineTemplate = "Tangaroa: {} {}, matariki: {}"
        if displayMonthLenght:
            lineTemplate += ", Lm: {}"
        for y in years:
            new_moons = getNewMoonAroundMatariki(y, observer=obs)
            t = getMatarikiTangaroa(y, new_moons, observer=obs)
            m = getMatarikiFriday(y, newMoons=new_moons, tangaroa=t, observer=obs)
            lineContent = [t.strftime('%Y %d %b'), t.strftime('%a'), m.strftime('%d %b')]
            if displayMonthLenght:
                lineContent.append(getLunarMonthLength(new_moons))
            print(lineTemplate.format(*lineContent))

if __name__=='__main__':
    displayMatarikiHolidays(range(2022,2053), displayMonthLenght=True)
