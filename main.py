from matariki import *

def displayMatarikiHolidays(years, observers=['500'], displayMonthLength=False, simpleMode=False):
    divider = '****************************************'
    for obs in observers:
        if not simpleMode:
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
            if simpleMode:
                print(m.isoformat().split('T')[0])
            else:
                lineContent = [t.strftime('%Y %d %b'), t.strftime('%a'), m.strftime('%d %b')]
                if displayMonthLength:
                    lineContent.append(getLunarMonthLength(new_moons))
                print(lineTemplate.format(*lineContent))
        if not simpleMode:
            print(divider)

if __name__=='__main__':
    displayMatarikiHolidays([122, 1057, 1884, 2178, 3866], observers=['467'], displayMonthLength=True, simpleMode=True)
