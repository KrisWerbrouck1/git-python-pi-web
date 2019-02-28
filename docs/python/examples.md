# Examples

## Mersenne primes
```python
def is_prime(numberToCheck):
  if numberToCheck <= 1:
      return False
  
  for divisor in range(2, numberToCheck):
      if numberToCheck % divisor == 0:
        return False
    
  return True

def potential_MP(exponent):
    return 2**exponent-1

print("Welcome to our Python Mersenne Prime Finder script")
numberToCheck = int(input("Please enter the number of Mersenne Primes to find: "))

print("The first", numberToCheck, "Mersenne Primes: ")
mps_found = 0
number = 3
while mps_found < numberToCheck:
    mp = potential_MP(number)
    if is_prime(mp):
        mps_found += 1
        print(str(mp), end=' ')
    number +=1
```

## LED class

```python
# The Led class instantiates a led on a pin
# State of the led can be on or off
class Led:
  def __init__(self, pin):
    self.pinNumber = pin
    self.off()

  def on(self):
    self.set_state(True)

  def off(self):
    self.set_state(False)

  def toggle(self):
    self.set_state(not self.get_state())
    return self.get_state()

  def set_state(self, state):
    self.isOn = state
    
  def get_state(self):
    return self.isOn

myLed = Led(1)
myLed.on()
print(myLed.get_state())
myLed.off()
print(myLed.get_state())
print(myLed.toggle())
print(myLed.toggle())
```