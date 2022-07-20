from datetime import datetime
import arrow

# JPLFORMAT = "YYYY-MMM-DD HH:mm:ss.SSS"
JPLFORMAT = "YYYY-MMM-DD HH:mm"
TIMEZONE = "Pacific/Auckland"

def arrow2str(t):
    return t.to('UTC').format(JPLFORMAT)

def str2arrow(s):
    return arrow.get(s, JPLFORMAT).to(TIMEZONE)
