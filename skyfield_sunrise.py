"""
2020-03-24
explore the skyfield module
https://rhodesmill.org/skyfield/
goal: print sunrise at a given location and date
"""

from skyfield import api
from skyfield import almanac
from datetime import timedelta

def find_sunrise(n=1):
    """
    Search the almanac for sunrise and sunset times in the next 24 hours.
    Does not actually compute the times.
    It looks them up in the precomputed ephemeris files provided by the JPL.
    Sunrise times are 'True', Sunset times are 'False'. Times are UTC. 
    """
    ts = api.load.timescale()
    ep = api.load('de421.bsp')
    location = api.Topos('41.85 N', '87.65 W') # Chicago, USA
    t0 = ts.now()
    t1 = ts.utc(t0.utc_datetime() + timedelta(days=n))
    t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(ep, location))
    
    times = list(zip(t.utc_iso(), y))
    print(times)


def Skyfield_Syntax_Notes():
    """Do not use this function. For reference only."""
    print('Do not use this function. For reference only.')
    
    if False:
        from skyfield import api
        from skyfield import almanac
        
        ts = api.load.timescale()
        # load the timescale object
        
        ep = api.load('de421.bsp')
        # load the JPL ephemeris
        # loads a local copy if present, otherwise downloads it from JPL.
        
        ts.now()
        # <Time tt=2458934.384140176>
        # return type: class
        
        ts.now().utc
        # (2020, 3, 25, 21, 14, 30.965784788131714)
        # return type: tuple

        ts.now().utc[:3]
        # (2020, 3, 25)
        # use slice to get only the year, month, and day
            
        ts.now().utc_iso()
        # '2020-03-25T21:13:53Z'
        # return type: str
    
        t0 = ts.now().utc[:3]
        t1 = t0[:2] + (t0[2] + 1,)
        # use now, utc, and slice to create date tuple of today
        # use slice and concat to create date tuple of tomorrow
        # ERROR this produces tuples, skyfield times are time objects
        # TODO figure out how to convert tuples back to time objects
        # DONE see next structure
        
        from datetime import timedelta
        t0 = ts.now()
        # start with skyfield time object
        t1 = ts.utc(t0.utc_datetime() + timedelta(days=1))
        # create new time object and use datetime.timedelta to increment the day
        
        
        
