from numberdisplay import NumberDisplay

number = NumberDisplay(24)

number.setValue(10)
print(number.getValue())

for i in range(10):
    number.increment()
    print(number.getDisplayValue())

