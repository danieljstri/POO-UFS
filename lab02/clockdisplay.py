
from numberdisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
     self.__hours = NumberDisplay(24)
     self.__minutes = NumberDisplay(60)
     self.__displayString = 0
     self.updateDisplay()

    def timeTick(self):
        self.__minutes.increment()
        if (self.__minutes.getValue() == 0):
           self.__hours.increment()
        self.updateDisplay()

    def updateDisplay(self):
        self.__displayString = self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue()

    def getTime(self):
        return self.__displayString

    def setTime(self, hours, minutes):
        self.__hours.setValue(hours)
        self.__minutes.setValue(minutes)
        self.updateDisplay()
