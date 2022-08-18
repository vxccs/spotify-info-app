import re
import datetime

# uses regex to extract the item type and id
def parse_url(URL):
    re_1 = "open\.spotify\.com/(?P<type>.+)/(?P<id>[a-zA-Z0-9]+).*$"
    re_2 = "spotify:(?P<type>.+):(?P<id>[a-zA-Z0-9]+).*$"
    
    if re.search(re_1, URL):
        return re.search(re_1, URL).groupdict()
    elif re.search(re_2, URL):
        return re.search(re_2, URL).groupdict()

# takes miliseconds and returns a formatted hh:mm:ss string
def sectomins(ms):
    ms = int(ms) / 1000
    mins, secs = divmod(ms, 60)
    hrs, mins = divmod(mins,60)
    if hrs == 0:
        return f"{int(mins):2d}:{int(secs):02d}"
    else:
        return f"{int(hrs):02d}:{int(mins):02d}:{int(secs):02d}"

# takes miliseconds and returns a formatted Hours Minutes Seconds string
def sectomins_format(ms):
    ms = int(ms) / 1000
    mins, secs = divmod(ms, 60)
    hrs, mins = divmod(mins,60)

    if hrs < 1:
        hours = ""
    elif hrs == 1:
        hours = f"{int(hrs)} hr"
    elif hrs > 1:
        hours = f"{int(hrs)} hrs"

    if mins < 1:
        minutes = ""
    elif mins == 1:
        minutes = f"{int(mins)} min"
    elif mins > 1:
        minutes = f"{int(mins)} mins"

    if secs < 1:
        seconds = ""
    elif secs == 1:
        seconds = f"{int(secs)} seco"
    elif secs > 1:
        seconds = f"{int(secs)} secs"
    
    if hours:
        return f"{hours} {minutes}"
    else:
        return f"{minutes} {seconds}"

# takes a date and formats it into Day Month, Year
def date_format(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return date.strftime("%-d %B, %Y")

# returns the correct mode for its id
def mode_format(mode):
    if mode == 0:
        return "Minor"
    if mode == 1:
        return "Major"

# formats numbers at 2 decimals
def decimals_format(value):
    return f"{value:.2f}"

# return the correct pitch class based on key and mode
def key_format(key, mode):
    modes = {(0,1):'8B',(1,1):'3B',(2,1):'10B',(3,1):'5B',(4,1):'12B',(5,1):'7B',(6,1):'2B',(7,1):'9B',(8,1):'4B',(9,1):'11B',(10,1):'6B',(11,1):'1B',(0,0):'5A',(1,0):'12A',(2,0):'7A',(3,0):'2A',(4,0):'9A',(5,0):'4A',(6,0):'11A',(7,0):'6A',(8,0):'1A',(9,0):'8A',(10,0):'3A',(11,0):'10A'}
    pitches = {'8B':'C, B♯','3B':'C♯, D♭','10B':'D','5B':'D♯, E♭','12B':'E','7B':'F','2B':'F♯, G♭','9B':'G','4B':'G♯, A♭','11B':'A','6B':'A♯, B♭','1B':'B','5A':'Cm','12A':'D♭m','7A':'Dm','2A':'E♭m','9A':'Em','4A':'Fm','11A':'G♭m','6A':'Gm','1A':'A♭m','8A':'Am','3A':'B♭m','10A':'Bm'}
    return pitches[modes[key, mode]]