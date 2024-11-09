"""GMT Converting"""

obsvr_time = input()
obsvr_gmt = float(input())
target_gmt = float(input())

time, AM_PM = obsvr_time.split(" ")
hr, m = map(int, time.split(":"))

delta_gmt = target_gmt - obsvr_gmt
if delta_gmt < 0:
    #delta_gmt += 12
    delta_gmt_hr = int(delta_gmt)
    delta_gmt_min = delta_gmt - delta_gmt_hr
    if AM_PM == "A.M.":
        AM_PM = "P.M."
    elif AM_PM == "P.M.":
        AM_PM = "A.M."
    if delta_gmt_min >= 0.6:
        delta_gmt_hr += 1
        delta_gmt_min -= 0.6
    elif delta_gmt_min <= -0.6:
        delta_gmt_hr -= 1
        delta_gmt_min += 0.6

    TTIME_HR = hr + delta_gmt_hr + 12
    TTIME_MIN = int(round(m + delta_gmt_min * 100))
else:
    delta_gmt_hr = int(delta_gmt)
    delta_gmt_min = delta_gmt - delta_gmt_hr

    if delta_gmt_min >= 0.6:
        delta_gmt_hr += 1
        delta_gmt_min -= 0.6
    elif delta_gmt_min <= -0.6:
        delta_gmt_hr -= 1
        delta_gmt_min += 0.6
    TTIME_HR = hr + delta_gmt_hr
    TTIME_MIN = int(round(m + (delta_gmt_min * 100)))

if TTIME_HR >= 12:
    if TTIME_HR > 12:
        TTIME_HR -= 12
    if AM_PM == "A.M." and hr != 12:
        AM_PM = "P.M."
    elif AM_PM == "P.M." and hr != 12:
        AM_PM = "A.M."
elif not TTIME_HR:
    TTIME_HR = 12

if TTIME_MIN >= 60:
    TTIME_HR += 1
    TTIME_MIN -= 60
elif TTIME_MIN < 0:
    TTIME_MIN += 60
    TTIME_HR -= 1
    if TTIME_HR == 11:
        if AM_PM == "A.M.":
            AM_PM = "P.M."
        elif AM_PM == "P.M.":
            AM_PM = "A.M."

print(f"{TTIME_HR:02}:{TTIME_MIN:02} {AM_PM}")