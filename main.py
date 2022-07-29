from matariki import *

def displayMatarikiHolidays(years, observers=['500']):
    for obs in observers:
        print()
        print('****************************************')
        print("Observer location: {}".format("Auckland Observatrory" if obs == '467' else "geocentric"))
        print('****************************************')
        for y in years:
            new_moons = getNewMoonAroundMatariki(y, observer=obs)
            t = getMatarikiTangaroa(y, new_moons, observer=obs)
            m = getMatarikiFriday(y, newMoons=new_moons, tangaroa=t, observer=obs)
            print("Tangaroa: {}, {}, matariki: {}"
              .format(t.strftime('%Y %d %b'), t.strftime('%a'), m.strftime('%d %b')))

if __name__=='__main__':
    displayMatarikiHolidays(range(2022,2053))
