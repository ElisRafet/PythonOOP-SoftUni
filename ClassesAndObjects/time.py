class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 00
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 00
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 00
        return self.get_time()

