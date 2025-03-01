import time
import math

print("Sample Input:")
number = int(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
result = math.sqrt(number)

print(f"Square root of {number} after {milliseconds} miliseconds is {result}")