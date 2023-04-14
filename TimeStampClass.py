class TimeStamp:

    def __init__(self, **units):
        self.hour = 0
        self.minute = 0
        self.second = 0
        for key, value in units.items():
            match key:
                case "hour":
                    self.hour = int(value)
                case "minute":
                    self.minute = int(value)
                case "second":
                    self.second = int(value)

#    def is_negative(self):
#        return not self.n_flag

    def gettime(self):
        return '{0}:{1}:{2}'.format(self.hour,self.minute,self.second)

    def showtime(self):
        print('{0}:{1}:{2}'.format(self.hour,self.minute,self.second))


def test():
    t = TimeStamp(hour="1",minute="2",second=3)
    #t.showtime()


test()
