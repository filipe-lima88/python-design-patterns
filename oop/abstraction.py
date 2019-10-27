#  Class with abstraction of 'add' operation:
class Adder:
    def __init__(self):
        self.sum = 0

    def add(self, value):
        self.sum += value


#  We don't need to know how 'add' works to use it!
acu = Adder()
for i in range(99):
    acu.add(i)
print(acu.sum)
