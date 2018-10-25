class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours, self.minutes, self.seconds = int(hours), int(minutes), int(seconds)
    
    def str_update(self, string):
        self.hours, self.minutes, self.seconds = string.split(":")
    
    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(int(self.hours), int(self.minutes), int(self.seconds))
    
    def add_clocks(self, clock):
        new_sec = int(self.seconds) + int(clock.seconds)
        new_min = int(self.minutes) + int(clock.minutes)
        new_hour = int(self.hours) + int(clock.hours)

        div_sec = divmod(new_sec, 60)
        new_sec = div_sec[1]
        new_min += div_sec[0]

        div_min = divmod(new_min, 60)
        new_min = div_min[1]

        div_hour = divmod(new_hour, 24)
        new_hour = div_hour[1]
        new_hour += div_min[0]

        clock3 = Clock(new_hour, new_min, new_sec)

        return clock3
