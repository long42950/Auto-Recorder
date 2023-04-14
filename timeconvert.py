import TimeStampClass

def to_second(stamp):
    return (stamp.hour*60+stamp.minute)*60+stamp.second

def to_minute(stamp):
    return stamp.hour*60+stamp.minute+stamp.second/60

def to_hour(stamp):
    return stamp.hour+(stamp.minute+stamp.second/60)/60
