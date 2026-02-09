# Write your code here
class Time:
    def __init__(self,hours,mins,seconds):
        self.__hours=hours
        self.__mins=mins
        self.__seconds=seconds
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self,value):
        if value>=0 and value<=23:
            self.__hours=value
        else:
             raise ValueError("Not Possible")
    @property
    def mins(self):
        return self.__mins
    @mins.setter
    def mins(self,value):
        if value>=0 and value<=59:
            self.__mins=value
        else:
            raise ValueError("Not Possible")
    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self,value):
        if value>=0 and value<=59:
            self.__seconds=value
        else:
            raise ValueError("Not Possible")
    
a=Time(0,0,0)
a.hours=4
a.mins=62
a.seconds=19
print(a.seconds)