from clockdisplay import ClockDisplay

clock = ClockDisplay()

clock.setTime(13, 45)
clock.updateDisplay()
print(clock.getTime())

for i in range(10):
    clock.timeTick()
    clock.updateDisplay()
    print(clock.getTime())