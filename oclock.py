class Time:
    def __init__(self, day, hour, minute, seconds):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.seconds = seconds
        
    staticmethod
    def from_dict(time_dict):
        return Time(time_dict['d'], time_dict['h'], time_dict['m'], time_dict['s'])
    
    def to_dict(self):
        return {'d': self.day, 'h': self.hour, 'm': self.minute, 's': self.seconds}
    
    def __sub__(self, other):
        result = Time(self.day - other.day, self.hour - other.hour, self.minute - other.minute, self.seconds - other.seconds)
        if result.seconds < 0:
            result.seconds += 60
            result.minute -= 1
        if result.minute < 0:
            result.minute += 60
            result.hour -= 1
        if result.hour < 0:
            result.hour += 24
            result.day -= 1
        return result
        
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.seconds}"


t1 = {"d": 0, "h": 9, "m" : 25, "s": 35}
t2 = {"d": 0, "h": 7, "m": 35, "s": 20}

time1 = Time.from_dict(t1)
time2 = Time.from_dict(t2)
result_time = time1 - time2
print(result_time)